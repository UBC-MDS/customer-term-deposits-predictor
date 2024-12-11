import pandas as pd
import pandera as pa
from pandera import Column, Check

def validate_data(input_path):
    """
    Validates the data in a CSV file against a predefined schema.

    This function reads data from the specified CSV file and validates its structure,
    data types, and value constraints using a Pandera schema. If the data violates
    any of the schema rules, the function raises appropriate errors.

    Parameters
    ----------
    input_path : str
        The path to the CSV file containing the data to be validated.

    Schema Validation Rules
    ------------------------
    - `age`: Integer, between 18 and 95, not nullable.
    - `balance`: Integer, not nullable.
    - `day`: Integer, between 1 and 31, not nullable.
    - `campaign`: Integer, greater than or equal to 1, not nullable.
    - `pdays`: Integer, nullable (can contain NaN).
    - `previous`: Integer, greater than or equal to 0, not nullable.
    - `job`: String, not nullable.
    - `marital`: String, not nullable.
    - `education`: String, not nullable.
    - `housing`: String, must be "yes" or "no".
    - `loan`: String, must be "yes" or "no".
    - `contact`: String, not nullable.
    - `month`: String, must be one of "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec".
    - `y`: String, must be "yes" or "no".

    Additional Checks
    -----------------
    - Ensures no duplicate rows in the dataset.

    Raises
    ------
    pandera.errors.SchemaError
        If the data does not conform to the schema.

    Example
    -------
    >>> validate_data("data.csv")
    Data validation passed.
    """
    data = pd.read_csv(input_path)

    schema = pa.DataFrameSchema({
        "age": pa.Column(int, pa.Check.between(18, 95), nullable=False),
        "balance": pa.Column(int, nullable=False),
        "day": pa.Column(int, pa.Check.between(1, 31), nullable=False),
        "campaign": pa.Column(int, pa.Check.greater_than_or_equal_to(1), nullable=False),
        "pdays": pa.Column(int, nullable=True),  # Updated to allow NaN (float type)
        "previous": pa.Column(int, pa.Check.greater_than_or_equal_to(0), nullable=False),
        "job": pa.Column(str, nullable=False),
        "marital": pa.Column(str, nullable=False),
        "education": pa.Column(str, nullable=False),
        "housing": pa.Column(str, Check.isin(["yes", "no"])),
        "loan": pa.Column(str, Check.isin(["yes", "no"])),
        "contact": pa.Column(str, nullable=False),
        "month": pa.Column(str, pa.Check.isin(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])),
        "y": pa.Column(str, pa.Check.isin(["yes", "no"]))
    },
    checks=[
        pa.Check(lambda df: ~df.duplicated().any(), error="Duplicate rows found.")  # Enforce uniqueness
    ])

    schema.validate(data, lazy=True)
    print("Data validation passed.")

if __name__ == '__main__':
    validate_data()
