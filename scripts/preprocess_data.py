import pandas as pd
import click

@click.command()
@click.option('--input_path', type=str, help='Path to the cleaned data CSV file.')
@click.option('--output_path', type=str, help='Path to save the preprocessed data CSV file.')
def preprocess_data(input_path, output_path):
    # Load the cleaned data
    data = pd.read_csv(input_path)

    # Convert target variable to binary
    data['y'] = data['y'].apply(lambda x: 1 if x == 'yes' else 0)

    # Binary conversion for columns
    binary_columns = ['default', 'housing', 'loan']
    for col in binary_columns:
        data[col] = data[col].apply(lambda x: 1 if x == 'yes' else 0)

    # One-hot encoding for categorical columns
    categorical_columns = ['job', 'marital', 'education', 'contact', 'month']
    data = pd.get_dummies(data, columns=categorical_columns, drop_first=True)

    # Save the preprocessed data
    data.to_csv(output_path, index=False)
    print(f"Preprocessed data saved to {output_path}")

if __name__ == '__main__':
    preprocess_data()
