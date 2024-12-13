import requests
import zipfile
import os
import shutil

def read_zip(url, download_zip_file1, zip_path, file_path, zip_file_name):
    """
    Downloads and extracts a ZIP file, including nested ZIP archives.

    This function downloads a ZIP file from the specified URL (if provided) or reads it 
    from a local file path, extracts its contents, and handles nested ZIP files by extracting 
    them into the specified directory.

    Parameters
    ----------
    url : str or None
        The URL to download the ZIP file from. If None, the function reads the ZIP file 
        from the `download_zip_file1` path directly.
    download_zip_file1 : str
        The path to save the downloaded ZIP file or the path to the local ZIP file to be extracted.
    zip_path : str
        The directory where the outer ZIP file will be extracted.
    file_path : str
        The directory where the nested ZIP file will be extracted.
    zip_file_name : str
        The name of the nested ZIP file within the outer ZIP archive to extract.

    Raises
    ------
    FileNotFoundError
        If the nested ZIP file (`zip_file_name`) is not found within the extracted contents of the outer ZIP.
    zipfile.BadZipFile
        If the file is not a valid ZIP archive or the ZIP file is corrupted.
    requests.exceptions.RequestException
        If there is an issue with the HTTP request when downloading the ZIP file.

    Notes
    -----
    - This function performs cleanup by removing intermediate directories and downloaded files after 
      extraction is complete.
    - The function assumes that the nested ZIP file (`zip_file_name`) exists within the outer ZIP archive.

    Examples
    --------
    Example 1: Using a URL to download and extract a ZIP file
    >>> read_zip(
    ...     url="https://example.com/test.zip",
    ...     download_zip_file1="downloads/test.zip",
    ...     zip_path="extracted/outer",
    ...     file_path="extracted/inner",
    ...     zip_file_name="nested.zip"
    ... )

    Example 2: Using a local ZIP file for extraction
    >>> read_zip(
    ...     url=None,
    ...     download_zip_file1="local/path/test.zip",
    ...     zip_path="extracted/outer",
    ...     file_path="extracted/inner",
    ...     zip_file_name="nested.zip"
    ... )
    """   
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
