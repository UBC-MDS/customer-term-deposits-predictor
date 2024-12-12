import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn import set_config
import os
import sys
from sklearn.metrics import classification_report
import click
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.evaluate_plot import generate_evaluation_plots


@click.command()
@click.option('--x-test-data', type=str, help="Path to test data features")
@click.option('--y-test-data', type=str, help="Path to test data target")
@click.option('--plot-to', type=str, help="Path to directory where the plot will be written to")

def main(x_test_data, y_test_data, plot_to):
    set_config(transform_output="pandas")
    # read in data
    X_test = pd.read_csv(x_test_data)
    y_test = pd.read_csv(y_test_data)
    #read in scaler
    with open("results/models/scaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)

    #transform x_test
    X_test_scaled = scaler.transform(X_test)
    pd.DataFrame(X_test_scaled).to_csv("data/processed/X_test_scaled.csv")

    #read in model
    with open("results/models/logistic_regression_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

    #predict
    y_pred = model.predict(X_test_scaled)

    #Save metric table    
    report_dict = classification_report(y_test, y_pred, output_dict=True)
    pd.DataFrame(report_dict).to_csv("results/tables/metrics.csv")

    # Generate evaluation plots
    generate_evaluation_plots(
        model=model,
        X_test_scaled=X_test_scaled,
        y_test=y_test,
        plot_to=plot_to,
        model_name="Logistic Regression Model"
    )

if __name__ == '__main__':
    main()