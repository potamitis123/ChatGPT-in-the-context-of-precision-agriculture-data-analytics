# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('collective.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Extracting hour from the Timestamp
df['Hour'] = df['Timestamp'].dt.hour

# Grouping data by date and hour, then calculating the sum of Counts
hourly_counts = df.groupby([df['Timestamp'].dt.date, 'Hour']).agg({'Counts': 'sum'}).reset_index()

# Pivot the data for heatmap, rows represent hours, columns represent dates, values represent Counts
heatmap_data = hourly_counts.pivot_table(values='Counts', index='Hour', columns=df['Timestamp'].dt.date, fill_value=0)

# Creating the heatmap
plt.figure(figsize=(15, 7))
plt.imshow(heatmap_data, aspect='auto', cmap='YlGnBu')
plt.colorbar(label='Insect Counts')
plt.xlabel('Dates')
plt.ylabel('Hours of the Day')
plt.title('Heatmap of Insect Activity (Circadian Rhythm)')
plt.xticks(ticks=range(len(heatmap_data.columns)), labels=[str(x) for x in heatmap_data.columns], rotation=90)
plt.yticks(ticks=range(24))
plt.tight_layout()
plt.show()
