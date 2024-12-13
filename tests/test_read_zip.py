import pytest
import os
import sys
import shutil
import zipfile
from unittest.mock import patch
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_zip import read_zip

# Test fixture to create a nested ZIP structure
def create_nested_zip(root_dir, outer_zip_path, inner_zip_name):
    inner_zip_path = os.path.join(root_dir, inner_zip_name)
    
    # Create inner ZIP file
    with zipfile.ZipFile(inner_zip_path, 'w') as inner_zip:
        inner_zip.writestr('test_file.txt', 'This is a test file.')

    # Create outer ZIP file containing the inner ZIP
    with zipfile.ZipFile(outer_zip_path, 'w') as outer_zip:
        outer_zip.write(inner_zip_path, arcname=inner_zip_name)

# Fixture to create temporary directories and ZIP files
@pytest.fixture
def setup_local_zip():
    temp_dir = os.path.join('tests', 'temp')
    os.makedirs(temp_dir, exist_ok=True)

    download_zip_file = os.path.join(temp_dir, 'test_outer.zip')
    zip_path = os.path.join(temp_dir, 'extracted')
    file_path = os.path.join(temp_dir, 'final')
    
    create_nested_zip(temp_dir, download_zip_file, 'inner.zip')

    yield download_zip_file, zip_path, file_path

    # Cleanup
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

# Test function: Local ZIP file
def test_read_zip_local(setup_local_zip):
    download_zip_file, zip_path, file_path = setup_local_zip
    url = None  # Not used for local tests

    read_zip(url, download_zip_file, zip_path, file_path, 'inner.zip')

    # Assert extracted content
    extracted_file = os.path.join(file_path, 'test_file.txt')
    assert os.path.exists(extracted_file), "Extracted file does not exist."
    with open(extracted_file, 'r') as f:
        content = f.read()
        assert content == 'This is a test file.', "File content mismatch."

# Test: Mocked HTTP response
@patch('requests.get')
def test_read_zip_remote(mock_get, setup_local_zip):
    download_zip_file, zip_path, file_path = setup_local_zip
    url = 'http://example.com/test_outer.zip'

    # Mock the HTTP response
    with open(download_zip_file, 'rb') as f:
        mock_get.return_value.content = f.read()

    read_zip(url, download_zip_file, zip_path, file_path, 'inner.zip')

    # Assert extracted content
    extracted_file = os.path.join(file_path, 'test_file.txt')
    assert os.path.exists(extracted_file), "Extracted file does not exist."
    with open(extracted_file, 'r') as f:
        content = f.read()
        assert content == 'This is a test file.', "File content mismatch."

# Test: Empty ZIP file
def test_empty_zip():
    temp_dir = os.path.join('tests', 'temp')
    os.makedirs(temp_dir, exist_ok=True)
    empty_zip_path = os.path.join(temp_dir, 'empty.zip')

    # Create an empty ZIP file
    with zipfile.ZipFile(empty_zip_path, 'w'):
        pass

    with pytest.raises(FileNotFoundError):
        read_zip(None, empty_zip_path, temp_dir, temp_dir, 'nonexistent.zip')

    shutil.rmtree(temp_dir)

# Test: Missing outer ZIP file
def test_missing_outer_zip():
    temp_dir = os.path.join('tests', 'temp')
    missing_zip_path = os.path.join(temp_dir, 'missing.zip')
    
    with pytest.raises(FileNotFoundError):
        read_zip(None, missing_zip_path, temp_dir, temp_dir, 'inner.zip')

# Test: Invalid ZIP format
def test_invalid_zip_format():
    temp_dir = os.path.join('tests', 'temp')
    invalid_zip_path = os.path.join(temp_dir, 'invalid.zip')
    os.makedirs(temp_dir, exist_ok=True)

    with open(invalid_zip_path, 'w') as f:
        f.write("This is not a ZIP file.")

    with pytest.raises(zipfile.BadZipFile):
        read_zip(None, invalid_zip_path, temp_dir, temp_dir, 'inner.zip')

    shutil.rmtree(temp_dir)