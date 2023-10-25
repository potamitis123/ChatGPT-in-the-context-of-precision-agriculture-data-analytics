# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""

import pandas as pd
import scipy.stats as stats

# Example usage:
file_path = 'collective.csv'
data = pd.read_csv(file_path)

from geopy.distance import geodesic
import itertools

# Getting unique trap locations
unique_traps = data[['Name', 'Lat', 'Long']].drop_duplicates().reset_index(drop=True)

# Function to calculate distance between two traps
def calculate_distance(row1, row2):
    coords_1 = (row1['Lat'], row1['Long'])
    coords_2 = (row2['Lat'], row2['Long'])
    return geodesic(coords_1, coords_2).kilometers

# Identifying adjacent traps within 1 km
adjacent_traps = []

for (index1, row1), (index2, row2) in itertools.combinations(unique_traps.iterrows(), 2):
    distance = calculate_distance(row1, row2)
    if distance <= 1:
        adjacent_traps.append((row1['Name'], row2['Name']))

adjacent_traps[:5], len(adjacent_traps)  # Displaying the first few adjacent pairs and total number of pairs

import scipy.stats as stats

# Creating a DataFrame to store the insect counts for adjacent traps
adjacent_data = pd.DataFrame()

for trap1, trap2 in adjacent_traps:
    # Getting data for each trap in the pair
    data_trap1 = data[data['Name'] == trap1]['Counts'].reset_index(drop=True)
    data_trap2 = data[data['Name'] == trap2]['Counts'].reset_index(drop=True)
    
    # Storing the data with trap pair as the column name
    adjacent_data[f'Trap_{trap1}_vs_{trap2}'] = pd.concat([data_trap1, data_trap2], ignore_index=True)

# Performing ANOVA
anova_results = stats.f_oneway(*[adjacent_data[col].dropna() for col in adjacent_data.columns])

anova_results


