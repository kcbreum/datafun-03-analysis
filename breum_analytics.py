""" This module demonstrates the fetching of data, processing it using Python collections, and writing the processed data to different file formats """

# Standard library imports
import csv
import pathlib
import logging
from io import StringIO

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
import logging
import requests
import csv
from io import StringIO

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
                csv_writer.writerow(movie_tuple)  # Write the row to the CSV file

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
    