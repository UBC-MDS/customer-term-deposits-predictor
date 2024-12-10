import click
import pandas as pd
import requests
import zipfile
import os
import shutil

@click.command()
@click.option('--url', type=str, help='URL to download the dataset')
@click.option('--download_zip_file1', type=str, help='path to load first zipfile')
@click.option('--zip_path', type=str, help='path to first file')
@click.option('--download_zip_file2', type=str, help='path to load second zipfile')
@click.option('--file_path', type=str, help='path to save file')

def main(url, download_zip_file1, zip_path, download_zip_file2, file_path):
     
    response = requests.get(url)
    os.makedirs(os.path.dirname(download_zip_file1), exist_ok=True)
    with open(download_zip_file1, 'wb') as f:
        f.write(response.content)


    with zipfile.ZipFile(download_zip_file1, 'r') as zip_ref:
        zip_ref.extractall(zip_path)


    nested_zip_path = os.path.join(zip_path, "bank.zip")
    with zipfile.ZipFile(nested_zip_path, 'r') as nested_zip_ref:
        nested_zip_ref.extractall(file_path)


    shutil.rmtree(zip_path) 
    os.remove(download_zip_file1)  

    # Load the data
    data = pd.read_csv(download_zip_file2, sep=';')

    # Preview the first few rows
    data.head()

if __name__ == '__main__':
    main()
