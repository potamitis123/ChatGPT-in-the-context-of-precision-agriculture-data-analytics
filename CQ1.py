# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT
"""

import folium
import pandas as pd

def visualize_unique_trap_locations(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Get unique trap locations
    unique_locations = data[['Lat', 'Long']].drop_duplicates()
    num_unique_locations = len(unique_locations)
    
    # Create a base world map
    world_map = folium.Map(location=[20,0], zoom_start=2, tiles='OpenStreetMap')
    
    # Add unique trap locations to the map
    for _, row in unique_locations.iterrows():
        folium.Marker([row['Lat'], row['Long']]).add_to(world_map)
    
    return world_map, num_unique_locations

# Visualizing unique trap locations on a world map
world_map, num_unique_locations = visualize_unique_trap_locations('collective.csv')
world_map, num_unique_locations

world_map.save('out.html')
