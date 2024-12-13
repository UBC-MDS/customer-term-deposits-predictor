import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import os
import sys
import pytest
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.split_data import split_data

#Creata a sample dataframe
@pytest.fixture
def valid_data():
    return pd.DataFrame({
        'x1': [1, 2, 3, 4, 5],
        'x2': [10, 20, 30, 40, 50],
        'y': [0, 1, 0, 1, 0]
    })

@pytest.fixture
def temp_dir(tmpdir):
    return tmpdir

def test_split_data_invalid_testing_size(temp_dir, valid_data):
    # Save the valid_data DataFrame to a temporary CSV file
    input_file = os.path.join(temp_dir, "valid_data.csv")
    valid_data.to_csv(input_file, index=False)

    # Try to split with an invalid testing_size (greater than 1)
    with pytest.raises(ValueError) as excinfo:
        split_data(input_file, str(temp_dir), testing_size=1.5)

    # Check if the correct error message is raised
    assert str(excinfo.value) == "testing_size must be between 0 and 1."

# Test for missing 'y' column in input data
def test_split_data_missing_target_column(temp_dir, valid_data):
    # Save the dataframe with the missing 'y' column to a CSV file
    data_missing_target = valid_data.drop(columns=["y"])  # Drop the 'y' column to simulate missing target
    input_file = os.path.join(temp_dir, "data_missing_target.csv")
    data_missing_target.to_csv(input_file, index=False)

    # Ensure that split_data raises a KeyError when 'y' is missing
    with pytest.raises(KeyError) as excinfo:
        split_data(input_file, str(temp_dir), testing_size=0.4)

    # Check if the exception message contains the expected string
    assert "The dataset must contain a column named 'y' as the target variable." in str(excinfo.value)

# Test for empty DataFrame
def test_split_data_empty_dataframe(temp_dir, valid_data):
    # Save an empty dataframe to a temporary CSV file
    empty_data = valid_data.iloc[0:0]  # This will create an empty DataFrame
    input_file = os.path.join(temp_dir, "empty_data.csv")
    empty_data.to_csv(input_file, index=False)

    # Ensure that split_data raises a ValueError when the dataset is empty
    with pytest.raises(ValueError) as excinfo:
        split_data(input_file, str(temp_dir), testing_size=0.4)

    # Check if the exception message contains the expected string
    assert "With n_samples=0" in str(excinfo.value)  # Checking for the error raised when input is empty

# Test for random state consistency
def test_split_data_random_state(temp_dir, valid_data):
    # Save the valid_data DataFrame to a temporary CSV file
    input_file = os.path.join(temp_dir, "valid_data.csv")
    valid_data.to_csv(input_file, index=False)

    # First split with a specific random_state
    split_data(input_file, str(temp_dir), testing_size=0.4)

    # Read the saved files and compare the train/test splits
    X_train_file_1 = os.path.join(temp_dir, "X_train.csv")
    X_test_file_1 = os.path.join(temp_dir, "X_test.csv")
    y_train_file_1 = os.path.join(temp_dir, "y_train.csv")
    y_test_file_1 = os.path.join(temp_dir, "y_test.csv")

    # Second split with the same random_state
    split_data(input_file, str(temp_dir), testing_size=0.4)

    # Read the saved files again to compare
    X_train_file_2 = os.path.join(temp_dir, "X_train.csv")
    X_test_file_2 = os.path.join(temp_dir, "X_test.csv")
    y_train_file_2 = os.path.join(temp_dir, "y_train.csv")
    y_test_file_2 = os.path.join(temp_dir, "y_test.csv")

    # Assert that the splits are identical for both runs
    assert pd.read_csv(X_train_file_1).equals(pd.read_csv(X_train_file_2)), "X_train split is not consistent"
    assert pd.read_csv(X_test_file_1).equals(pd.read_csv(X_test_file_2)), "X_test split is not consistent"
    assert pd.read_csv(y_train_file_1).equals(pd.read_csv(y_train_file_2)), "y_train split is not consistent"
    assert pd.read_csv(y_test_file_1).equals(pd.read_csv(y_test_file_2)), "y_test split is not consistent"

def test_split_data_non_existent_input_file(temp_dir):
    # Use a non-existent file path
    non_existent_file = "/path/to/nonexistent/file.csv"

    # Ensure that split_data raises a FileNotFoundError when the input file doesn't exist
    with pytest.raises(FileNotFoundError) as excinfo:
        split_data(non_existent_file, str(temp_dir), testing_size=0.4)

    # Check if the exception message matches the expected string
    assert "The input file path does not exist or cannot be found." in str(excinfo.value)