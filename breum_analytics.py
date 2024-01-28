""" This module demonstrates the fetching of data, processing it using Python collections, and writing the processed data to different file formats """

# Standard library imports
import csv
import xlwt
import pathlib
import logging
from io import StringIO
import json

# External library imports
import requests

# Local module imports
import breum_projsetup
import utils_breum

# Define Functions
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch data: {response.status_code}")

def fetch_and_write_csv_data(folder_name, filename, url):
    response == requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch CSV data: {response.status_code}")

def fetch_and_write_excel_data(folder_name, filename, url):
    response == requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch Excel data: {response.status_code}")

def fetch_and_write_json_data(folder_name, filename, url):
    response == requests.get(url)
    if response.status_code == 200:
        # Call your write function to save the response content
        pass
    else:
        print(f"Failed to fetch JSON data: {response.status_code}")

def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

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



# Function 1: Process text data
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



# Function 2: Process CSV Data
logging.basicConfig(level=logging.INFO)

file_path = 'movies.csv'
url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv'

try:
    response = requests.get(url)
    if response.status_code == 200:
        logging.info('Successfully fetched the movie data.')
        movie_data = response.content.decode('utf-8')
        csv_reader = csv.reader(StringIO(movie_data))

        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            for row in csv_reader:
                movie_tuple = tuple(row)
                csv_writer.writerow(movie_tuple)

                title, year, genre, rank, rating, director, actors, runtime, votes, revenue, metascore, description = movie_tuple

                logging.debug(f"Title: {title}")
                logging.debug(f"Year: {year}")
                logging.debug(f"Genre: {genre}")
                logging.debug(f"Director: {director}")
                logging.debug(f"Rating: {rating}")

    else:
        logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')

except FileNotFoundError:
    logging.error(f"File not found: {file_path}")

except Exception as e:
    logging.error(f"Error occurred: {e}")

# Unique genres
csv_file_path = 'movies.csv'
text_file_path = 'unique_genres.txt'

try:
    response = requests.get(url)
    if response.status_code ==200:
        movie_data = response.content.decode('utf-8')
        csv_reader = csv.reader(StringIO(movie_data))

        unique_genres = set()
        next(csv_reader)
        for row in csv_reader:
            title, year, genre, rank, rating, director, actors, runtime, votes, revenue, metascore, description = row
            unique_genres.add(genre)
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            for genre in unique_genres:
                text_file.write(f"{genre}\n")
except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')

except FileNotFoundError:
    logging.error(f"File not found: {csv_file_path}")

except Exception as e:
    logging.error(f"Error occurred: {e}")



# Function 3: Process Excel Data
logging.basicConfig(level=logging.INFO)

file_path = 'wine.xls'
url = 'https://raw.githubusercontent.com/kying18/wine-classification/master/winequality-red.csv'

try:
    response = requests.get(url)
    if response.status_code == 200:
        logging.info('Successfully fetched the wine data.')
        wine_data = response.text
        csv_reader = csv.reader(StringIO(wine_data), delimiter=';')

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('Wine Data')

        header = next(csv_reader)
        for col_num, col_name in enumerate(header):
            sheet.write(0, col_num, col_name)

        for row_num, row in enumerate(csv_reader, start=1):
            for col_num, value in enumerate(row):
                sheet.write(row_num, col_num, value)

        workbook.save(file_path)
        logging.info(f'Excel file "{file_path}" created successfully.')

    else:
        logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')

except FileNotFoundError:
    logging.error(f"File not found: {file_path}")

except Exception as e:
    logging.error(f"Error occurred: {e}")

# Analyzing to list wine quality over 5
import logging
import xlrd

logging.basicConfig(level=logging.INFO)

excel_file_path = 'wine.xls'
text_file_path = 'quality_above_5.txt'

try:
    workbook = xlrd.open_workbook(excel_file_path)
    sheet = workbook.sheet_by_name('Wine Data')

    quality_column_index = sheet.row_values(0).index('quality')

    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        for row_num in range(1, sheet.nrows):
            quality_value = sheet.cell_value(row_num, quality_column_index)
            if quality_value >= 5:
                row_data = sheet.row_values(row_num)
                text_file.write(','.join(map(str, row_data)) + '\n')

    logging.info(f'Filtered data written to "{text_file_path}".')

except FileNotFoundError:
    logging.error(f"File not found: {excel_file_path}")

except Exception as e:
    logging.error(f"Error occurred: {e}")



# Function 4: Process JSON Data    
api_url = 'http://api.open-notify.org/astros.json'
weather_data = fetch_weather_data(api_url)
if weather_data:
    save_json(weather_data, 'weather_data.json')
    saved_weather_data = read_json('weather_data.json')
    print(saved_weather_data)



# Main function
def main():
    ''' Main function to demonstrate module capabilities'''
    print(f"Name: {utils_breum.my_name_string}")

    txt_url = 'https://www.gutenberg.org/cache/epub/1342/pg1342-images.html'

    csv_url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv'

    excel_url = 'https://raw.githubusercontent.com/kying18/wine-classification/master/winequality-red.csv'

    json_url = 'http://api.open-notify.org/astros.json'