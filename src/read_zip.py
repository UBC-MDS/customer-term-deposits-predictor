import click
import pandas as pd
import requests
import zipfile
import os
import shutil

def read_zip(url, download_zip_file1, zip_path, file_path, zip_file_name):
     
    response = requests.get(url)
    os.makedirs(os.path.dirname(download_zip_file1), exist_ok=True)
    with open(download_zip_file1, 'wb') as f:
        f.write(response.content)


    with zipfile.ZipFile(download_zip_file1, 'r') as zip_ref:
        zip_ref.extractall(zip_path)

    nested_zip_path = os.path.join(zip_path, zip_file_name)
    with zipfile.ZipFile(nested_zip_path, 'r') as nested_zip_ref:
        nested_zip_ref.extractall(file_path)


    shutil.rmtree(zip_path) 
    os.remove(download_zip_file1)  

if __name__ == '__main__':
    read_zip()
