# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 00:13:16 2023

@author: INSECTRONICS
Retrieving insect counts and environmental data from the E-funnel insect trap  
"""

# E-funnel read data
import requests
import pandas as pd

# API endpoint and parameters
api_url = 'https://insectronics.net/api/v1/get_device/861340049519018'
params = {
    'from': '2023-02-16',
    'to': '2023-02-20',
    'token': 'INSECTRONICS_API_KEY'
}

# Send the GET request to the API
response = requests.get(api_url, params=params, verify=True)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the device data
    device_data = data['device']
    # Create a DataFrame for the device data
    device_df = pd.DataFrame([device_data])
    
    # Extract the measurements
    measurements_data = data['measurements']
    # Create a list to hold measurement records
    measurement_records = []
    # Iterate over the measurements and prepare a record for each
    for timestamp, measurements in measurements_data.items():
        record = measurements.copy()  # Copy the measurements to avoid modifying the original data
        record['timestamp'] = pd.to_datetime(timestamp, unit='s')  # Add the timestamp as a field in the record
        measurement_records.append(record)
    
    # Create a DataFrame for the measurement records
    measurements_df = pd.DataFrame(measurement_records)
    
    # Merge the device and measurements dataframes
    # This will add the device information as columns to each measurement record
    result_df = pd.concat([device_df]*len(measurements_df), ignore_index=True)
    result_df = pd.concat([result_df, measurements_df], axis=1)
    
    # Print the resulting DataFrame
    print(result_df)
else:
    print('Failed to retrieve data:', response.status_code)