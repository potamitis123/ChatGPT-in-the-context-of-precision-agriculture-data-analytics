# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 18:48:14 2023

@author: ChatGPT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('collective.csv')

# Defining bins for Temperature and Humidity
temperature_bins = [-np.inf, 10, 20, 30, 40, np.inf]
humidity_bins = [-np.inf, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, np.inf]

# Categorizing the data into the defined bins
data['Temperature_Bin'] = pd.cut(data['Temperature'], bins=temperature_bins)
data['Humidity_Bin'] = pd.cut(data['Humidity'], bins=humidity_bins)

# Grouping by the bins and calculating the mean counts
average_counts_temp = data.groupby('Temperature_Bin')['Counts'].mean().reset_index()
average_counts_humidity = data.groupby('Humidity_Bin')['Counts'].mean().reset_index()

# Visualizing the results
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

# Temperature
axs[0].bar(average_counts_temp['Temperature_Bin'].astype(str), average_counts_temp['Counts'])
axs[0].set_xlabel('Temperature (°C)')
axs[0].set_ylabel('Average Counts')
axs[0].set_title('Average Counts by Temperature Bins')
axs[0].tick_params(axis='x', rotation=45)

# Humidity
axs[1].bar(average_counts_humidity['Humidity_Bin'].astype(str), average_counts_humidity['Counts'])
axs[1].set_xlabel('Humidity (%)')
axs[1].set_ylabel('Average Counts')
axs[1].set_title('Average Counts by Humidity Bins')
axs[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
