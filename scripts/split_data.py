import pandas as pd
from sklearn.model_selection import train_test_split
import click

@click.command()
@click.option('--input_path', type=str, help='Path to the preprocessed data CSV file.')
@click.option('--output_train_x', type=str, help='Path to save the training features.')
@click.option('--output_train_y', type=str, help='Path to save the training labels.')
@click.option('--output_test_x', type=str, help='Path to save the testing features.')
@click.option('--output_test_y', type=str, help='Path to save the testing labels.')
def split_data(input_path, output_train_x, output_train_y, output_test_x, output_test_y):
    # Load preprocessed data
    data = pd.read_csv(input_path)

    # Separate features and target
    X = data.drop(columns=['y'])
    y = data['y']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Save split data
    X_train.to_csv(output_train_x, index=False)
    X_test.to_csv(output_test_x, index=False)
    y_train.to_csv(output_train_y, index=False)
    y_test.to_csv(output_test_y, index=False)

    print(f"Training and testing sets saved to:\n- {output_train_x}\n- {output_train_y}\n- {output_test_x}\n- {output_test_y}")

if __name__ == '__main__':
    split_data()
