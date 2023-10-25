# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT
"""

import pandas as pd
import folium
import folium.plugins as plugins

def visualize_counts_heatmap_greece(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Define approximate latitude and longitude bounds for Greece
    lat_bounds = [34.5, 42]
    long_bounds = [19, 30]
    
    # Filter the data to only include points within Greece
    greece_data = data[(data['Lat'] >= lat_bounds[0]) & (data['Lat'] <= lat_bounds[1]) & 
                       (data['Long'] >= long_bounds[0]) & (data['Long'] <= long_bounds[1])]
    
    # Create a base map of Greece
    greece_map = folium.Map(location=[37.9838, 23.7275], zoom_start=6, tiles='OpenStreetMap')
    
    # Prepare data for the heatmap
    heat_data = [[row['Lat'], row['Long'], row['Counts']] for _, row in greece_data.iterrows()]
    
    # Overlay heatmap on the Greece map
    plugins.HeatMap(heat_data, radius=15).add_to(greece_map)
    
    greece_map.save('heatmap_greece_output.html')

# To run the function, use:
#file_path = 'path_to_your_file.csv'
visualize_counts_heatmap_greece('collective.csv')