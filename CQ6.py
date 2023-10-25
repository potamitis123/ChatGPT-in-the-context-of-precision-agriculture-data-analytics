# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: user ChatGPT
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'collective.csv'

data = pd.read_csv(file_path)
data['Timestamp'] = pd.to_datetime(data['Timestamp'])
data['Hour'] = data['Timestamp'].dt.hour

# Extracting month and day from the Timestamp to use as labels on the x-axis
data['Month_Day'] = data['Timestamp'].dt.strftime('%m-%d')

# Creating pivot tables for Humidity and Temperature
humidity_pivot = data.pivot_table(values='Humidity', index='Hour', columns='Month_Day')
temperature_pivot = data.pivot_table(values='Temperature', index='Hour', columns='Month_Day')

# Plotting
fig, axs = plt.subplots(2, 1, figsize=(15, 10), sharex=True)

# Heatmap for Humidity
sns.heatmap(data=humidity_pivot, ax=axs[0], cmap='YlGnBu', vmin=0, vmax=100, cbar_kws={'label': 'Humidity (%)'})
axs[0].set_title('Humidity Heatmap')
axs[0].set_ylabel('Hour')

# Heatmap for Temperature
sns.heatmap(data=temperature_pivot, ax=axs[1], cmap='YlOrRd', vmin=0, vmax=60, cbar_kws={'label': 'Temperature (°C)'})
axs[1].set_title('Temperature Heatmap')
axs[1].set_xlabel('Month-Day')
axs[1].set_ylabel('Hour')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()