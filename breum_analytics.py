""" This module demonstrates the fetching of data, processing it using Python collections, and writing the processed data to different file formats """

# Standard library imports
import csv
import pathlib

# External library imports
import requests

# Local module imports
import breum_projsetup
import utils_breum

# Data acquisition
import requests

def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response == requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

# Write data
from pathlib import Path

def write_text_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) #use pathlib to join paths
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

def write_excel_file(folder_name, filename, data):
    file_path = Path(folder_name).join_path(filename) #use pathlib to join paths
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"Excel data saved to {file_path}")
        