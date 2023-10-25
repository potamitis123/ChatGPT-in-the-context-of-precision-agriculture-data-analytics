# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""

import pandas as pd

# Function to get the location of a specific trap
def get_trap_location(trap_name, dataframe):
    location = dataframe[dataframe['Name'] == trap_name][['Lat', 'Long']].iloc[-1]
    return location['Lat'], location['Long']

# Load the dataset
file_path = 'collective.csv'  # Update this to the path of your CSV file
data = pd.read_csv(file_path)

# Converting 'Timestamp' to datetime format
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extracting date and hour from 'Timestamp'
data['Date'] = data['Timestamp'].dt.date
data['Hour'] = data['Timestamp'].dt.hour
data['Week'] = data['Timestamp'].dt.isocalendar().week

# Hourly counts
max_hourly_count = data.loc[data['Counts'].idxmax()]
min_hourly_count = data.loc[data['Counts'].idxmin()]

# Daily counts
daily_counts = data.groupby(['Name', 'Date'])['Counts'].sum().reset_index()
max_daily_count = daily_counts.loc[daily_counts['Counts'].idxmax()]
min_daily_count = daily_counts.loc[daily_counts['Counts'].idxmin()]

# Weekly counts
weekly_counts = data.groupby(['Name', 'Week'])['Counts'].sum().reset_index()
max_weekly_count = weekly_counts.loc[weekly_counts['Counts'].idxmax()]
min_weekly_count = weekly_counts.loc[weekly_counts['Counts'].idxmin()]

# Outputting the results
print(f"Highest hourly count: Trap {max_hourly_count['Name']} at location ({get_trap_location(max_hourly_count['Name'], data)}) with {max_hourly_count['Counts']} insects.")
print(f"Lowest hourly count: Trap {min_hourly_count['Name']} at location ({get_trap_location(min_hourly_count['Name'], data)}) with {min_hourly_count['Counts']} insects.")
print(f"Highest daily count: Trap {max_daily_count['Name']} at location ({get_trap_location(max_daily_count['Name'], data)}) with {max_daily_count['Counts']} insects.")
print(f"Lowest daily count: Trap {min_daily_count['Name']} at location ({get_trap_location(min_daily_count['Name'], data)}) with {min_daily_count['Counts']} insects.")
print(f"Highest weekly count: Trap {max_weekly_count['Name']} at location ({get_trap_location(max_weekly_count['Name'], data)}) with {max_weekly_count['Counts']} insects.")
print(f"Lowest weekly count: Trap {min_weekly_count['Name']} at location ({get_trap_location(min_weekly_count['Name'], data)}) with {min_weekly_count['Counts']} insects.")
