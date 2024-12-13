import requests
import zipfile
import os
import shutil

def read_zip(url, download_zip_file1, zip_path, file_path, zip_file_name):
    # Only fetch the file from URL if the URL is not None
    if url:
        response = requests.get(url)
        os.makedirs(os.path.dirname(download_zip_file1), exist_ok=True)
        with open(download_zip_file1, 'wb') as f:
            f.write(response.content)
    
    # Extract the outer ZIP file
    with zipfile.ZipFile(download_zip_file1, 'r') as zip_ref:
        zip_ref.extractall(zip_path)

    # Extract the nested ZIP file
    nested_zip_path = os.path.join(zip_path, zip_file_name)
    with zipfile.ZipFile(nested_zip_path, 'r') as nested_zip_ref:
        nested_zip_ref.extractall(file_path)

    # Cleanup intermediate files
    shutil.rmtree(zip_path)
    if url:  # Only remove the downloaded file if it was fetched from a URL
        os.remove(download_zip_file1)
