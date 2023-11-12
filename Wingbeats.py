# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:41:02 2023

@author: INSECTRONICS
Retrieving wav recordings from the WINGBEATS device (insects' wingbeat recorder)  
"""

# Wingbeats recorder download data from INSECTRONICS, unzip folder, read wav files
import os
import requests
import zipfile
import librosa

# Directory to extract wav files
EXTRACT_FOLDER = 'wav_files'

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

def get_wav_filenames(directory):
    # List all files in the directory and filter out non-wav files
    return [f for f in os.listdir(directory) if f.endswith('.wav')]

def load_wav_file(filename, directory):
    # Load the wav file using librosa
    file_path = os.path.join(directory, filename)
    return librosa.load(file_path, sr=None)  # sr=None to preserve original sampling rate


# API endpoint and parameters
api_url = 'https://insectronics.net/api/v1/get_binaries/565374519850399'
params = {
    'from': '2022-11-13',
    'to': '2022-11-29',
    'token': 'INSECTRONICS_API_KEY'
}

# Download the zip file from the API
zip_filename = download_zip(api_url, params)  # Uncomment this line when running locally

# Unzip the wav files
unzip_files(zip_filename, EXTRACT_FOLDER)

# Get list of wav filenames
wav_filenames = get_wav_filenames(EXTRACT_FOLDER)

# Load and process wav files one by one
wav_files_data = []
for wav_filename in wav_filenames:
    y, sr = load_wav_file(wav_filename, EXTRACT_FOLDER)
    wav_files_data.append((y, sr))
    print(f"Loaded {wav_filename} with sample rate {sr}")



