import click
import pandas as pd
import requests
import zipfile
import os
import shutil

@click.command()
@click.option('--url', type=str, help='...')
@click.option('--path1', type=str, help='...')
@click.option('--path2', type=str, help='...')
@click.option('--path3', type=str, help='...')
@click.option('--path4', type=str, help='...')

def main(url, path1, path2, path3, path4):
     
    response = requests.get(url)
    os.makedirs(os.path.dirname(path1), exist_ok=True)
    with open(path1, 'wb') as f:
        f.write(response.content)


    with zipfile.ZipFile(path1, 'r') as zip_ref:
        zip_ref.extractall(path2)


    nested_zip_path = os.path.join(path2, "bank.zip")
    with zipfile.ZipFile(nested_zip_path, 'r') as nested_zip_ref:
        nested_zip_ref.extractall(path4)


    shutil.rmtree(path2) 
    os.remove(path1)  

    # Load the data
    data = pd.read_csv(path3, sep=';')

    # Preview the first few rows
    data.head()

if __name__ == '__main__':
    main()
