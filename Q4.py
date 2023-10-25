# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualize_temp_humidity_correlation(file_path, num_traps=5):
    # Load the dataset
    data = pd.read_csv(file_path)
    
    # Get a list of unique trap IDs and randomly select a subset
    trap_ids = np.random.choice(data['Name'].unique(), size=num_traps, replace=False)
    
    # Create a subplot for each trap
    fig, axes = plt.subplots(nrows=num_traps, figsize=(10, 4*num_traps))
    
    for i, trap_id in enumerate(trap_ids):
        trap_data = data[data['Name'] == trap_id]
        
        # Compute the Pearson correlation coefficient
        correlation = trap_data['Temperature'].corr(trap_data['Humidity'])
        
        # Scatter plot for temperature vs humidity
        axes[i].scatter(trap_data['Temperature'], trap_data['Humidity'], alpha=0.5)
        axes[i].set_title(f"Trap ID: {trap_id} | Correlation: {correlation:.2f}")
        axes[i].set_xlabel('Temperature')
        axes[i].set_ylabel('Humidity')
        axes[i].grid(True)

    plt.tight_layout()
    plt.show()

# Visualizing temperature-humidity correlation for five randomly selected traps
visualize_temp_humidity_correlation('collective.csv')
