import os
from sklearn.metrics import ConfusionMatrixDisplay, PrecisionRecallDisplay, RocCurveDisplay
import matplotlib.pyplot as plt

def generate_evaluation_plots(model, X_test_scaled, y_test, plot_to, model_name="Model"):
    """
    Generates and saves confusion matrix, precision-recall, and ROC curve plots.
    
    Parameters
    ----------
        model: The trained model object.
        X_test_scaled: The scaled test features.
        y_test: The true labels for the test set.
        plot_to: Path to the directory where plots will be saved.
        model_name: Name of the model for labeling plots (default: "Model").

    Example
    -------
    >>> generate_evaluation_plots(model, X_test_scaled, y_test, plot_to="plots", model_name="Logistic Regression Model")
    plots are made
    """
    # Confusion Matrix
    ConfusionMatrixDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        values_format="d"
    )
    plt.title(f"Confusion Matrix: {model_name}")
    plt.savefig(os.path.join(plot_to, "Confusion_Matrix.png"))
    plt.close()

    # Precision-Recall Curve
    PrecisionRecallDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        pos_label=True,
        name=f'{model_name}'
    )
    plt.title(f"Precision-Recall Curve: {model_name}")
    plt.savefig(os.path.join(plot_to, "PR_curve.png"))
    plt.close()

    # ROC Curve
    RocCurveDisplay.from_estimator(
        model,
        X_test_scaled,
        y_test,
        pos_label=True,
        name=f'{model_name}'
    )
    plt.title(f"ROC Curve: {model_name}")
    plt.savefig(os.path.join(plot_to, "ROC_curve.png"))
    plt.close()

if __name__ == '__main__':
    generate_evaluation_plots()