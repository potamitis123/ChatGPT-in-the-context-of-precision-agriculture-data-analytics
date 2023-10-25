# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_insect_trends_over_time(file_path, num_traps=5, freq='D'):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Convert the 'Timestamp' column to datetime format
    data['Timestamp'] = pd.to_datetime(data['Timestamp'])
    
    # Group by trap ID and time interval, then aggregate insect counts
    grouped_data = data.groupby(['Name', pd.Grouper(key='Timestamp', freq=freq)]).agg({'Counts': 'sum'}).reset_index()
    
    # Get a list of unique trap IDs and randomly select a subset
    trap_ids = np.random.choice(data['Name'].unique(), size=num_traps, replace=False)
    
    # Plotting trends for each selected trap
    plt.figure(figsize=(15, 4*num_traps))
    
    for i, trap_id in enumerate(trap_ids):
        trap_data = grouped_data[grouped_data['Name'] == trap_id]
        
        plt.subplot(num_traps, 1, i+1)
        plt.plot(trap_data['Timestamp'], trap_data['Counts'], marker='o', linestyle='-', label=f'Trap {trap_id}')
        plt.title(f"Trap ID: {trap_id}")
        plt.xlabel('Time')
        plt.ylabel('Insect Counts')
        plt.grid(True)
        plt.legend()

    plt.tight_layout()
    plt.show()

# Visualizing insect count trends over time for five randomly selected traps
visualize_insect_trends_over_time('collective.csv')

