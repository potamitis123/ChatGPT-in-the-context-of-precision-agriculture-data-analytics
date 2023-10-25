# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: user
"""


from geopy.distance import geodesic
import pandas as pd

df = pd.read_csv('collective.csv')

# Coordinates of the center of Larissa
larissa_center = (39.6396, 22.4196)

# Dropping duplicate rows that have the same Name, Lat, and Long
unique_traps = df.drop_duplicates(subset=['Name', 'Lat', 'Long'])

# Calculating the distance of each unique trap to the center of Larissa
unique_traps['Distance_to_Larissa'] = unique_traps.apply(
    lambda row: geodesic(larissa_center, (row['Lat'], row['Long'])).kilometers, axis=1)

# Identifying the three closest unique traps to the center of Larissa
closest_unique_traps = unique_traps.nsmallest(3, 'Distance_to_Larissa')

# Displaying the three closest unique traps
closest_unique_traps[['Name', 'Lat', 'Long', 'Distance_to_Larissa']]


import pandas as pd

# Filtering the dataset to include only the three closest traps
closest_traps_data = df[df['Name'].isin(closest_unique_traps['Name'])]

# Pivoting the data to have trap names as columns, and filling NaN values with zero
pivot_data = closest_traps_data.pivot_table(values='Counts', index='Timestamp', columns='Name', fill_value=0)

# Performing cross-correlation analysis
cross_corr_matrix = pivot_data.corr()

# Displaying the cross-correlation matrix
cross_corr_matrix