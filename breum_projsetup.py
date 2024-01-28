''' This module provides functions for creating a series of project folders. '''

# Imported dependencies
import math
import statistics
from pathlib import Path
import utils_breum
import os
import time



# Defined functions for folder creation
def create_project_directory(directory_name: str):
    Path(directory_name).mkdir(exist_ok=True)

def create_annual_data_directories(directory_name: str, start_year: int, end_year: int):
    create_project_directory(directory_name)
    for year in range(start_year, end_year + 1):
        print(year)
        year_directory = Path(directory_name) / str(year)
        create_project_directory(year_directory)

def create_folders_from_list(folder_list, to_lowercase=False, remove_spaces=False):
    for folder_name in folder_list:
        if to_lowercase:
            folder_name = folder_name.lower()
        if remove_spaces:
            folder_name = folder_name.replace(" ", "")
        print(f"Processing folder: {folder_name}")

def create_prefixed_folders(folder_list, prefix):
    for folder_name in folder_list:
        folder_path = Path(prefix + folder_name)
        folder_path.mkdir(exist_ok=True)
folder_names = ['csv', 'excel', 'json']
prefix = 'data-'

def create_folders_periodically(duration_secs):
    pass
regions = ["North America", "South America", "Europe", "Asia", "Africa", "Oceania", "Middle East"]



# Defined main function
def main():
    print(f"Byline: {utils_breum.byline}")
    create_annual_data_directories('data', start_year=2014, end_year=2024)
    create_folders_from_list(folder_names)
    create_prefixed_folders(folder_names, prefix)
    create_folders_periodically(duration_secs=5)
    create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)



# Conditional script
if __name__ == '__main__':
    main()



# Help was received using AI for assistance with reviewing errors. All code was my own or from utilizing the Module 2 lesson