import pandas as pd
import numpy as np
import click

@click.command()
@click.option('--input_path', type=str, help='Path to the raw data CSV file.')
@click.option('--output_path', type=str, help='Path to save the cleaned data CSV file.')
def clean_data(input_path, output_path):
    # Load the data
    data = pd.read_csv(input_path, sep=';')

    # Replace "unknown" with NaN
    data.replace('unknown', np.nan, inplace=True)

    # Impute missing values
    data['job'] = data['job'].fillna(data['job'].mode()[0])
    data['education'] = data['education'].fillna(data['education'].mode()[0])
    data['contact'] = data['contact'].fillna('Unknown Contact')

    # Drop irrelevant columns
    data.drop(columns=['poutcome', 'duration'], inplace=True)

    # Remove duplicates
    data = data.drop_duplicates()

    # Save the cleaned data
    data.to_csv(output_path, index=False)

if __name__ == '__main__':
    clean_data()
