import click
import pandas as pd
import requests
import zipfile
import os
import shutil
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read_zip import read_zip

@click.command()
@click.option('--url', type=str, help='URL to download the dataset')
@click.option('--download_zip_file1', type=str, help='path to load first zipfile')
@click.option('--zip_path', type=str, help='path to first file')
@click.option('--file_path', type=str, help='path to save file')
@click.option('--zip_file_name', type=str, help='second zip file name')

def main(url, download_zip_file1, zip_path, file_path, zip_file_name):
     
    """Downloads data zip data from the web to a local filepath and extracts it."""
    try:
        read_zip(url, download_zip_file1, zip_path, file_path, zip_file_name)
    except:
        os.makedirs(download_zip_file1, zip_path, file_path)
        read_zip(url, download_zip_file1, zip_path, file_path, zip_file_name)

if __name__ == '__main__':
    main()



