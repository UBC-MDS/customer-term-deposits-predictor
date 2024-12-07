import click
import os
import altair as alt
import numpy as np
import pandas as pd
import pickle
from sklearn import set_config
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import requests
import zipfile
import os
import shutil
import altair as alt
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from deepchecks.tabular import Dataset
from deepchecks.tabular.checks import FeatureLabelCorrelation
from deepchecks.tabular.checks import FeatureFeatureCorrelation
import click

@click.command()
@click.option('--x-training-data', type=str, help="Path to training data features")
@click.option('--y-training-data', type=str, help="Path to training data target")
@click.option('--pipeline-to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--plot-to', type=str, help="Path to directory where the plot will be written to")
@click.option('--seed', type=int, help="Random seed", default=123)

def main(x_training_data, y_training_data, pipeline_to, plot_to, seed):
    np.random.seed(seed)
    set_config(transform_output="pandas")
    # read in data
    X_train = pd.read_csv(x_training_data)
    y_train = pd.read_csv(y_training_data)

    #using standardscalar
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    #save scaler
    scaler_path = os.path.join(pipeline_to, "scaler.pkl")
    with open(scaler_path, 'wb') as scaler_file:
        pickle.dump(scaler, scaler_file)

    #Save scaled files to preprocessed folder
    pd.DataFrame(X_train_scaled).to_csv("data/processed/X_train_scaled.csv")

    correlation_matrix = pd.DataFrame(X_train_scaled, columns=X_train.columns).corr()
    correlation_long = correlation_matrix.reset_index().melt(id_vars='index')
    correlation_long.columns = ['Feature 1', 'Feature 2', 'Correlation']

    plot = alt.Chart(correlation_long).mark_rect().encode(
        x='Feature 1:O',
        y='Feature 2:O',
        color=alt.Color('Correlation:Q', scale=alt.Scale(scheme='viridis')),
        tooltip=['Feature 1', 'Feature 2', 'Correlation']
    ).properties(
        width=600,
        height=600,
        title="Correlation Heatmap"
    )
    plot.save(os.path.join(plot_to, "feature_densities_by_class.png"), scale_factor=2.0)

    #mute warnings 
    warnings.filterwarnings("ignore", category=FutureWarning)

    train_data = pd.concat([pd.DataFrame(X_train_scaled, columns=X_train.columns), y_train], axis=1)
    train_melted = train_data.melt(id_vars=['y'], var_name='predictor', value_name='value')
    train_melted.replace([np.inf, -np.inf], np.nan, inplace=True)
    train_melted.dropna(inplace=True)

    # Define a function for kdeplot with hue
    def kdeplot_with_hue(data, **kwargs):
        sns.kdeplot(data=data, x='value', hue='y', fill=True, alpha=0.6, **kwargs)

    # Use map_dataframe instead of map
    g = sns.FacetGrid(train_melted, col='predictor', col_wrap=5, height=3, sharex=False, sharey=False)
    g.map_dataframe(kdeplot_with_hue)

    # Add titles and adjust layout
    g.set_titles("{col_name}")
    g.set_axis_labels("Value", "Density")
    g.fig.subplots_adjust(top=0.9)

    plt.savefig(os.path.join(plot_to, "facet_grid_plot.png"))

    # Combine X_train and y_train into a single dataset for analysis
    #train_data_with_target = X_train.copy()
    #train_data_with_target['y'] = y_train.reset_index(drop=True)
    y_train = y_train.rename(columns={y_train.columns[0]: 'y'})
    combined_data = pd.concat([X_train, y_train], axis=1)

    # Create a Deep Checks Dataset object
    deepchecks_dataset = Dataset(combined_data, label="y", cat_features=[])

    # Run the Feature-Label Correlation check
    feature_label_corr_check = FeatureLabelCorrelation().add_condition_feature_pps_less_than(0.9)
    feature_label_corr_result = feature_label_corr_check.run(deepchecks_dataset)

    # Run the Feature-Feature Correlation check
    feature_feature_corr_check = FeatureFeatureCorrelation().add_condition_max_number_of_pairs_above_threshold(threshold = 0.99, n_pairs = 0)
    feature_feature_corr_result = feature_feature_corr_check.run(deepchecks_dataset)

    if not feature_label_corr_result.passed_conditions():
        raise ValueError("Feature-Label correlation exceeds the maximum acceptable threshold.")

    if not feature_feature_corr_result.passed_conditions():
        raise ValueError("Feature-feature correlation exceeds the maximum acceptable threshold.")

    #Train Logistic Regression model
    model = LogisticRegression(class_weight='balanced', max_iter=1000)
    model.fit(X_train_scaled, y_train.values.ravel())

    #save model
    model_path = os.path.join(pipeline_to, "logistic_regression_model.pkl")
    with open(model_path, 'wb') as model_file:
        pickle.dump(model, model_file)

if __name__ == '__main__':
    main()