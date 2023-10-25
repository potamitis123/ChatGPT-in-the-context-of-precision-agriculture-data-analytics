# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 18:22:38 2023

@author: user
"""


import pandas as pd

# Load the dataset
file_path = 'collective.csv'
data = pd.read_csv(file_path)

# Convert the Timestamp column to datetime and extract the hour
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Hour'] = data['Timestamp'].dt.hour

# Function to identify outliers based on the IQR method
def identify_outliers(df):
    Q1 = df['Counts'].quantile(0.25)
    Q3 = df['Counts'].quantile(0.75)
    IQR = Q3 - Q1
    outlier_condition = (df['Counts'] > (Q3 + 1.5 * IQR))
    return df[outlier_condition]

# Filter data for trap ID 213 and time between 9:00 PM and 4:00 AM
filtered_data = data[(data['Name'] == 213) & ((data['Hour'] >= 21) | (data['Hour'] <= 4))]

# Group the filtered data by Hour and apply the outlier identification function
outliers = filtered_data.groupby('Hour').apply(identify_outliers)

# Resetting index for cleaner output and display the outliers
outliers.reset_index(drop=True, inplace=True)
print(outliers[['Timestamp', 'Counts', 'Hour']])

import matplotlib.pyplot as plt

# Grouping data by Hour and applying the outlier identification function
outliers = filtered_data.groupby('Hour').apply(identify_outliers)

# Plotting
plt.figure(figsize=(12, 6))

# Plotting all data points
plt.plot(filtered_data['Timestamp'], filtered_data['Counts'], marker='o', linestyle='-', color='grey', label='Counts', markersize=4)

# Highlighting the outliers
plt.plot(outliers['Timestamp'], outliers['Counts'], marker='o', linestyle=' ', color='red', label='Outliers', markersize=6)

# Formatting the plot
plt.title('Insect Counts in Trap ID 213 (9:00 PM - 4:00 AM)')
plt.xlabel('Timestamp')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()