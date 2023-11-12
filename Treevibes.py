# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:01:27 2023

@author: INSECTRONICS
Retrieving TreeVibe data and mp3 recordings from ones account
"""

# TreeVibe temperature and recording sessions
import requests
import pandas as pd

def get_device_measurements(api_url, params):
    # Make the GET request to the API
    response = requests.get(api_url, params=params, verify=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract measurements
        measurements_data = data['measurements']
        
        # Convert the measurements to a DataFrame
        timestamps = [int(ts) for ts in measurements_data.keys()]
        temperatures = [details['Temp'] for details in measurements_data.values()]
        
        # Create a DataFrame
        df = pd.DataFrame({
            'Timestamp': pd.to_datetime(timestamps, unit='s'),
            'Temperature': temperatures
        })
        
        return df
    else:
        # Handle errors
        response.raise_for_status()

# API endpoint and parameters
api_url = 'https://insectronics.net/api/v1/get_device/868822041632066'
params = {
    'from': '2023-06-15',
    'to': '2023-06-16',
    'token': 'INSECTRONICS_API_KEY'
}

# Call the function and print the DataFrame
device_measurements_df = get_device_measurements(api_url, params)
print(device_measurements_df)


# Retrieving data and mp3 recordings from ones account the audio signals
import requests
import zipfile
import os
from pydub import AudioSegment

# Function to download and unzip the mp3 files
def download_and_unzip_mp3(api_url, params, extract_to='mp3_files'):
    # Make the GET request to download the zip file
    response = requests.get(api_url, params=params, stream=True, verify=True)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the downloaded zip file to disk
        zip_filename = 'files.zip'
        with open(zip_filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=128):
                f.write(chunk)
        
        # Unzip the file
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(extract_to)

        # Get the list of mp3 filenames
        filenames = [filename for filename in os.listdir(extract_to) if filename.endswith('.mp3')]
        return filenames
    else:
        # Handle errors
        response.raise_for_status()

# Function to load mp3 files into memory
def load_mp3_files(filenames, directory='mp3_files'):
    mp3_files = []
    for filename in filenames:
        file_path = os.path.join(directory, filename)
        # Load the mp3 file
        audio = AudioSegment.from_mp3(file_path)
        mp3_files.append(audio)
    return mp3_files

# API endpoint and parameters
api_url = 'https://insectronics.net/api/v1/get_binaries/868822041632066'
params = {
    'from': '2023-06-15',
    'to': '2023-11-10',
    'token': 'INSECTRONICS_API_KEY'
}

# Download and unzip the mp3 files
filenames = download_and_unzip_mp3(api_url, params)

# Load the mp3 files
mp3_files = load_mp3_files(filenames)
print(f"Loaded {len(mp3_files)} MP3 files.")

# TreeVibe download data from INSECTRONICS, unzip folder, read mp3 files
# This script carries out the same tasks as the previous one without the pydub lib. It used the librosa lib 
import os
import requests
import zipfile
import librosa

# Directory to extract MP3 files
EXTRACT_FOLDER = 'mp3_files'

def download_zip(api_url, params):
    # Make the GET request to download the zip file
    response = requests.get(api_url, params=params, stream=True, verify=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the downloaded zip file to disk
        zip_filename = 'downloaded_files.zip'
        with open(zip_filename, 'wb') as zip_file:
            for chunk in response.iter_content(chunk_size=128):
                zip_file.write(chunk)
        return zip_filename
    else:
        response.raise_for_status()

def unzip_files(zip_filename, extract_to):
    # Unzip the file
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_filename)  # Remove the zip file after extraction

def get_mp3_filenames(directory):
    # List all files in the directory and filter out non-mp3 files
    return [f for f in os.listdir(directory) if f.endswith('.mp3')]

def load_mp3_file(filename, directory):
    # Load the mp3 file using librosa
    file_path = os.path.join(directory, filename)
    return librosa.load(file_path, sr=None)  # sr=None to preserve original sampling rate

# API endpoint and parameters
api_url = 'https://insectronics.net/api/v1/get_binaries/868822041632066'
params = {
    'from': '2023-06-15',
    'to': '2023-11-10',
    'token': 'INSECTRONICS_API_KEY'
}

# Download the zip file from the API
zip_filename = download_zip(api_url, params)  # Uncomment this line when running locally

# Unzip the MP3 files
unzip_files(zip_filename, EXTRACT_FOLDER)

# Get list of MP3 filenames
mp3_filenames = get_mp3_filenames(EXTRACT_FOLDER)

# Load and process MP3 files one by one
mp3_files_data = []
for mp3_filename in mp3_filenames:
    y, sr = load_mp3_file(mp3_filename, EXTRACT_FOLDER)
    mp3_files_data.append((y, sr))
    print(f"Loaded {mp3_filename} with sample rate {sr}")

# At this point, 'mp3_files_data' contains tuples of audio time series 'y' and sampling rate 'sr'


