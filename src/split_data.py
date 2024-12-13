import pandas as pd
from sklearn.model_selection import train_test_split
import click
import os
import sys

def split_data(input_path, output_path, testing_size):
    """
    Splits a dataset into training and testing sets and saves the split data to CSV files.

    This function loads a preprocessed dataset from the specified input path, separates 
    the features (X) and target (y), splits the data into X and y training, and X and y testing sets,
    and saves the resulting datasets into CSV files in the specified output directory.
    Note this function assumes the target column is labeled 'y'.

    Args:
        input_path (str): Path to the input CSV file containing the preprocessed dataset. 
                           The dataset is assumed to have features (X) and a target variable (y).
        output_path (str): Directory path where the training and testing data will be saved as CSV files.
                           The function will save `X_train.csv`, `X_test.csv`, `y_train.csv`, and `y_test.csv` 
                           in this directory.
        testing_size (float): Proportion of the dataset to include in the testing set. 
                              A value between 0 and 1 (e.g., 0.3 means 30% of the data will be used for testing).

    Returns:
        None

    Example:
        input_path = 'data/processed/preprocessed_data.csv'
        output_path = 'data/processed/'
        testing_size = 0.3

        split_data(input_path, output_path, testing_size)

    This will split the dataset from 'data/processed/preprocessed_data.csv' into training and testing sets, 
    with 30% of the data used for testing, and save the resulting datasets into the 'data/processed/' directory. 
    The function will create the following files:
        - 'X_train.csv': Features for the training set
        - 'X_test.csv': Features for the testing set
        - 'y_train.csv': Target values for the training set
        - 'y_test.csv': Target values for the testing set
    """
    # Ensure that the input file exists
    if not os.path.isfile(input_path):
        raise FileNotFoundError("The input file path does not exist or cannot be found.")

    # Load preprocessed data
    data = pd.read_csv(input_path)

    if 'y' not in data.columns:
        raise KeyError("The dataset must contain a column named 'y' as the target variable.")

    if not (0 < float(testing_size) < 1):
        raise ValueError("testing_size must be between 0 and 1.")

    # Separate features and target
    X = data.drop(columns=['y'])
    y = data['y']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(testing_size), random_state=42)

    # Save split data
    X_train.to_csv(f'{output_path}/X_train.csv', index=False)
    X_test.to_csv(f'{output_path}/X_test.csv', index=False)
    y_train.to_csv(f'{output_path}/y_train.csv', index=False)
    y_test.to_csv(f'{output_path}/y_test.csv', index=False)

    print(f"Training and testing sets saved to:\n- {output_path}")

if __name__ == '__main__':
    split_data()