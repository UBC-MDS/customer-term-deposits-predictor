import pytest
import pandas as pd
import numpy as np
import os
import sys
import tempfile
from pandera.errors import SchemaErrors
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.validate import validate_data

# Test fixture to create temporary CSV files
def create_temp_csv(data):
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    data.to_csv(temp_file.name, index=False)
    return temp_file.name

# Valid test data
def valid_data():
    return pd.DataFrame({
        "age": [25, 40, 60],
        "balance": [1000, 2000, 3000],
        "day": [15, 20, 10],
        "campaign": [1, 2, 3],
        "pdays": [10, 8, 5],
        "previous": [0, 1, 2],
        "job": ["admin", "technician", "manager"],
        "marital": ["married", "single", "divorced"],
        "education": ["primary", "secondary", "tertiary"],
        "housing": ["yes", "no", "yes"],
        "loan": ["no", "yes", "no"],
        "contact": ["cellular", "unknown", "telephone"],
        "month": ["jan", "feb", "mar"],
        "y": ["yes", "no", "yes"]
    })

# Case: Valid data should pass validation
def test_valid_data():
    data = valid_data()
    temp_file = create_temp_csv(data)
    try:
        validate_data(temp_file)
    except Exception as e:
        pytest.fail(f"Valid data raised an exception: {e}")
    finally:
        os.remove(temp_file)

# Case: Missing column
@pytest.mark.parametrize("missing_column", valid_data().columns)
def test_missing_column(missing_column):
    data = valid_data().drop(columns=[missing_column])
    temp_file = create_temp_csv(data)
    with pytest.raises(SchemaErrors):
        validate_data(temp_file)
    os.remove(temp_file)

# Case: Out-of-range values
out_of_range_cases = [
    ("age", -1),
    ("age", 100),
    ("day", 0),
    ("day", 32),
    ("campaign", 0),
    ("previous", -1)
]
@pytest.mark.parametrize("column,value", out_of_range_cases)
def test_out_of_range_values(column, value):
    data = valid_data()
    data.loc[0, column] = value
    temp_file = create_temp_csv(data)
    with pytest.raises(SchemaErrors):
        validate_data(temp_file)
    os.remove(temp_file)

# Case: Invalid categories
invalid_category_cases = [
    ("housing", "maybe"),
    ("loan", "unknown"),
    ("month", "abc"),
    ("y", "unknown")
]
@pytest.mark.parametrize("column,value", invalid_category_cases)
def test_invalid_categories(column, value):
    data = valid_data()
    data.loc[0, column] = value
    temp_file = create_temp_csv(data)
    with pytest.raises(SchemaErrors):
        validate_data(temp_file)
    os.remove(temp_file)

# Case: Wrong data type
wrong_type_cases = [
    ("age", "twenty"),           # Invalid string
    ("balance", "one_thousand"), # Invalid string
    ("day", "fifteenth"),        # Invalid string
    ("campaign", "first"),       # Invalid string
    ("previous", "zero")         # Invalid string
]
@pytest.mark.parametrize("column,value", wrong_type_cases)
def test_wrong_data_types(column, value):
    data = valid_data()
    # Cast column to `object` to suppress dtype warnings
    data[column] = data[column].astype(object)
    data.loc[0, column] = value  # Assign invalid value directly
    temp_file = create_temp_csv(data)
    with pytest.raises(SchemaErrors):
        validate_data(temp_file)
    os.remove(temp_file)

# Case: Empty file
def test_empty_file():
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
    temp_file.close()
    with pytest.raises(ValueError):
        validate_data(temp_file.name)
    os.remove(temp_file.name)

# Case: Duplicate rows
def test_duplicate_rows():
    data = valid_data()
    data = pd.concat([data, data.iloc[[0]]])  # Add a duplicate row
    temp_file = create_temp_csv(data)
    with pytest.raises(SchemaErrors):
        validate_data(temp_file)
    os.remove(temp_file)
