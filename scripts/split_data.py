import pandas as pd
from sklearn.model_selection import train_test_split
import click
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.split_data import split_data

@click.command()
@click.option('--input_path', type=str, help='Path to the preprocessed data CSV file.')
@click.option('--output_path', type=str, help='Path to save the train and test data.')
@click.option('--testing_size', type=str, help='Specify test file size')

def main(input_path, output_path, testing_size):

        split_data(input_path, output_path, float(testing_size))

if __name__ == '__main__':
    main()
