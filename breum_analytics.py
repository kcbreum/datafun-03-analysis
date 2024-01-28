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


# Process data and generate output

# Function 1: Process text data
import requests

url = 'https://www.gutenberg.org/cache/epub/1342/pg1342-images.html'
response = requests.get(url)
text = response.text.lower()

print(text)

# Word count
words = text.split()
words = [word for word in words if word.isalnum()]
unique_words = set(words)
with open('unique_words.txt', 'w') as file:
    for word in unique_words:
        file.write(word + '\n')

# Word frequency
words = text.split()
words = [word for word in words if word.isalnum()]
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1
with open('word_frequency.txt', 'w') as file:
    for word, frequency in word_frequency.items():
        file.write(f"{word}: {frequency}\n")

# Character count
character_count = len(text)

print(f"Character Count: {character_count}")

non_space_character_count = len([char for char in text if char != ' '])

print(f"Non-Space Character Count: {non_space_character_count}")

# Identification of Mr. Darcy
darcy_occurences = [word for word in words if word == 'darcy']

print("Occurrences of 'Mr. Darcy':", darcy_occurences)