# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT
"""

import pandas as pd

def compute_weekly_humidity_stats_italy(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Convert 'Date' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])

    # Extract week and year from 'Date' for grouping
    data['Year'] = data['Timestamp'].dt.year
    data['Week'] = data['Timestamp'].dt.week

    # Define approximate latitude and longitude bounds for Italy
    lat_bounds_italy = [35.5, 47.5]
    long_bounds_italy = [6.5, 18.5]

    # Filter for Italy based on these bounds
    italy_data = data[(data['Lat'] >= lat_bounds_italy[0]) & (data['Lat'] <= lat_bounds_italy[1]) & 
                      (data['Long'] >= long_bounds_italy[0]) & (data['Long'] <= long_bounds_italy[1])]

    # Group by trap ('Name'), year, week, and compute weekly insect counts and mean humidity for each group
    grouped_data = italy_data.groupby(['Name', 'Year', 'Week']).agg({'Counts': 'sum', 'Humidity': 'mean', 'Temperature': 'mean'}).reset_index()

    # Filter the grouped data for traps with weekly counts of more than 100 insects
    high_weekly_count_data = grouped_data[grouped_data['Counts'] > 100]

    # Compute average and standard deviation of humidity for these entries
    avg_humidity_weekly = high_weekly_count_data['Humidity'].mean()
    std_humidity_weekly = high_weekly_count_data['Humidity'].std()

    # Calculate the average temperature and its standard deviation
    avg_temperature_weekly = high_weekly_count_data['Temperature'].mean()
    std_temperature_weekly = high_weekly_count_data['Temperature'].std()
    
    (avg_temperature_weekly, std_temperature_weekly), (avg_humidity_weekly, std_humidity_weekly)
    
    return avg_humidity_weekly, std_humidity_weekly, avg_temperature_weekly, std_temperature_weekly

# To run the function, use:
file_path = 'collective.csv'
avg_humidity_weekly, std_humidity_weekly, avg_temperature_weekly, std_temperature_weekly = compute_weekly_humidity_stats_italy(file_path)

print("Average Weekly Humidity:", avg_humidity_weekly)
print("Standard Deviation of Weekly Humidity:", std_humidity_weekly)
print("Average Weekly temperature:", avg_temperature_weekly)
print("Standard Deviation of Weekly temperature:", std_temperature_weekly)
