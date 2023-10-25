# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 13:03:14 2023

@author: ChatGPT
"""

import matplotlib.pyplot as plt

# Converting the Timestamp column to datetime type
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extracting the hour from the Timestamp
data['Hour'] = data['Timestamp'].dt.hour

# Grouping by hour and calculating the mean for Counts, Temperature, and Humidity
hourly_data = data.groupby('Hour')[['Counts', 'Temperature', 'Humidity']].mean().reset_index()

# Plotting
fig, ax1 = plt.subplots(figsize=(10, 5))

# Plotting the Counts
color = 'tab:blue'
ax1.set_xlabel('Hour of the Day')
ax1.set_ylabel('Average Counts', color=color)
ax1.plot(hourly_data['Hour'], hourly_data['Counts'], color=color, marker='o')
ax1.tick_params(axis='y', labelcolor=color)

# Instantiating a second y-axis sharing the same x-axis
ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('Average Temperature (°C)', color=color)
ax2.plot(hourly_data['Hour'], hourly_data['Temperature'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

# Instantiating a third y-axis sharing the same x-axis
ax3 = ax1.twinx()
color = 'tab:green'
# Moving the spine to the right to avoid overlap
ax3.spines['right'].set_position(('outward', 60))
ax3.set_ylabel('Average Humidity (%)', color=color)
ax3.plot(hourly_data['Hour'], hourly_data['Humidity'], color=color, marker='o')
ax3.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('Average Hourly Counts, Temperature, and Humidity')
plt.show()
