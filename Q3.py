# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'collective.csv'  # Update this to the path of your CSV file
data = pd.read_csv(file_path)

# Setting random seed for reproducibility
np.random.seed(0)

# Getting unique trap names
unique_traps = data['Name'].unique()

# Randomly selecting five trap names
selected_traps = np.random.choice(unique_traps, size=5, replace=False)

# Extracting data for the selected traps
selected_data = data[data['Name'].isin(selected_traps)]

# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Creating a boxplot for the temperature values of each selected trap
plt.figure(figsize=(12, 7))
ax = sns.boxplot(x='Name', y='Temperature', data=selected_data, showfliers=False, notch=True)

# Overlaying the min and max temperature values
min_temperatures = selected_data.groupby('Name')['Temperature'].min().reset_index()
max_temperatures = selected_data.groupby('Name')['Temperature'].max().reset_index()

# Adding the min and max values to the plot
ax.scatter(min_temperatures.index, min_temperatures['Temperature'], color='red', label='Min Temperatures')
ax.scatter(max_temperatures.index, max_temperatures['Temperature'], color='blue', label='Max Temperatures')

# Adding titles and labels
plt.title('Temperature Distribution Across Different Traps')
plt.xlabel('Trap Name')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()
