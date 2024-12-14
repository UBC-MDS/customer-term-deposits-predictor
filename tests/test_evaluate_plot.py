import pytest
import os
import sys
import tempfile
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.evaluate_plot import generate_evaluation_plots 


# Test fixture to create temporary directories
@pytest.fixture
def temp_dir():
    temp_directory = tempfile.TemporaryDirectory()
    yield temp_directory.name
    temp_directory.cleanup()

# Test fixture for sample dataset and model
@pytest.fixture
def sample_model_and_data():
    X, y = make_classification(
        n_samples=100,
        n_features=20,
        n_classes=2,
        random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler().fit(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LogisticRegression().fit(X_train, y_train)
    return model, X_test_scaled, y_test

# Test case: Check that plots are generated
def test_generate_plots(temp_dir, sample_model_and_data):
    model, X_test_scaled, y_test = sample_model_and_data
    generate_evaluation_plots(
        model=model,
        X_test_scaled=X_test_scaled,
        y_test=y_test,
        plot_to=temp_dir,
        model_name="Test Model"
    )
    # Check if all plots are created
    assert os.path.exists(os.path.join(temp_dir, "Confusion_Matrix.png"))
    assert os.path.exists(os.path.join(temp_dir, "PR_curve.png"))
    assert os.path.exists(os.path.join(temp_dir, "ROC_curve.png"))

# Test case: Invalid model input
def test_invalid_model(temp_dir, sample_model_and_data):
    _, X_test_scaled, y_test = sample_model_and_data
    with pytest.raises(ValueError, match="The provided model is not a valid classifier."):
        generate_evaluation_plots(
            model=None,
            X_test_scaled=X_test_scaled,
            y_test=y_test,
            plot_to=temp_dir,
            model_name="Invalid Model"
        )

# Test case: Invalid data shapes
def test_invalid_data_shapes(temp_dir, sample_model_and_data):
    model, _, y_test = sample_model_and_data
    X_test_scaled_invalid = np.random.random((10, 10))  # Incorrect shape
    with pytest.raises(ValueError):
        generate_evaluation_plots(
            model=model,
            X_test_scaled=X_test_scaled_invalid,
            y_test=y_test,
            plot_to=temp_dir,
            model_name="Invalid Data Shape"
        )

# Test case: Missing labels
def test_missing_labels(temp_dir, sample_model_and_data):
    model, X_test_scaled, _ = sample_model_and_data
    y_test_missing = []  # Empty list for labels
    with pytest.raises(ValueError):
        generate_evaluation_plots(
            model=model,
            X_test_scaled=X_test_scaled,
            y_test=y_test_missing,
            plot_to=temp_dir,
            model_name="Missing Labels"
        )