# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 01:08:13 2023

@author: INSECTRONICS
Retrieving jpeg images from vision-based traps  
"""

import requests
import zipfile
import os
from PIL import Image

# The API endpoint
api_url = 'https://insectronics.net/api/v1/get_binaries/867280060721156'
params = {
    'from': '2023-09-01',
    'token': 'INSECTRONICS_API_KEY'
}

# The local path to save the downloaded zip file
zip_file_path = 'downloaded_images.zip'
# The directory to extract the images to
extract_to_dir = 'extracted_images'

# Call the API and download the zip file
response = requests.get(api_url, params=params, stream=True, verify=True)

# Check if the request was successful
if response.status_code == 200:
    # Save the zip file locally
    with open(zip_file_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=128):
            file.write(chunk)
    
    # Unzip the file to the directory
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    
    # List all jpeg files in the directory
    image_files = [f for f in os.listdir(extract_to_dir) if f.endswith('.jpeg') or f.endswith('.jpg')]

    # Read all images (optional step)
    images = [Image.open(os.path.join(extract_to_dir, img_file)) for img_file in image_files]

    print(f'{len(images)} images have been read.')
else:
    print('Failed to download the file:', response.status_code)

# At this point, `images` contains all the PIL Image objects for the JPEG images.
# You can process these images as needed.
