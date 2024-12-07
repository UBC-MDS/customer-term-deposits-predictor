import pandas as pd
import pandera as pa
from pandera import Column, Check
import click

@click.command()
@click.option('--input_path', type=str, help='Path to the cleaned data CSV file.')
def validate_data(input_path):
    data = pd.read_csv(input_path)

    schema = pa.DataFrameSchema({
        "age": pa.Column(int, pa.Check.between(18, 95), nullable=False),
        "balance": pa.Column(int, nullable=False),
        "day": pa.Column(int, pa.Check.between(1, 31), nullable=False),
        "campaign": pa.Column(int, pa.Check.greater_than_or_equal_to(1), nullable=False),
        "pdays": pa.Column(int, nullable=True),
        "previous": pa.Column(int, pa.Check.greater_than_or_equal_to(0), nullable=False),
        "job": pa.Column(str, nullable=False),
        "marital": pa.Column(str, nullable=False),
        "education": pa.Column(str, nullable=False),
        "housing": pa.Column(str, Check.isin(["yes", "no"])),
        "loan": pa.Column(str, Check.isin(["yes", "no"])),
        "contact": pa.Column(str, nullable=False),
        "month": pa.Column(str, pa.Check.isin(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])),
        "y": pa.Column(str, pa.Check.isin(["yes", "no"]))
    })

    schema.validate(data, lazy=True)
    print("Data validation passed.")

if __name__ == '__main__':
    validate_data()
