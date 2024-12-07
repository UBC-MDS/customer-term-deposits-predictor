import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn import set_config
import os
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay 
from sklearn.metrics import PrecisionRecallDisplay
from sklearn.metrics import RocCurveDisplay
import click


@click.command()
@click.option('--x-test-data', type=str, help="Path to test data features")
@click.option('--y-test-data', type=str, help="Path to test data target")
#@click.option('--pipeline-to', type=str, help="Path to directory where the pipeline object will be written to")
@click.option('--plot-to', type=str, help="Path to directory where the plot will be written to")
#@click.option('--seed', type=int, help="Random seed", default=123)

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

    #Confusion matrix
    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        values_format="d"
    )
    plt.title("Confusion Matrix: Logistic Regression Model")
    plt.savefig(os.path.join(plot_to, "Confusion_Matrix.png"))

    #Precision-Recall
    PrecisionRecallDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        pos_label=True,
        name='Logistic Regression Model'
    )
    plt.title("Precision-Recall Curve")
    plt.savefig(os.path.join(plot_to, "PR_curve.png"))

    #ROC
    RocCurveDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        pos_label=True,
        name='Logistic Regression Model'
    )
    plt.title("ROC Curve")
    plt.savefig(os.path.join(plot_to, "ROC_curve.png"))


if __name__ == '__main__':
    main()