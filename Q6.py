# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT4-Plus
"""
import pandas as pd
import matplotlib.pyplot as plt


data = df = pd.read_csv('collective.csv')

# Converting 'Timestamp' to datetime format for the entire dataset
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# Extracting the date from the 'Timestamp' column
data['Date'] = data['Timestamp'].dt.date

# Calculating the total daily counts for each trap
daily_counts = data.groupby(['Name', 'Date'])['Counts'].sum().reset_index()

# Calculating the average daily counts for each trap
average_daily_counts = daily_counts.groupby('Name')['Counts'].mean().reset_index()

# Sorting the traps by average daily counts in descending order
average_daily_counts.sort_values(by='Counts', ascending=False, inplace=True)

# Selecting the first ten traps with the highest average daily counts
top_ten_traps = average_daily_counts.head(10)

# Visualizing the average daily counts for the top ten traps in ordered priority
plt.figure(figsize=(10, 6))
sns.barplot(x='Name', y='Counts', data=top_ten_traps, palette='viridis', order=top_ten_traps['Name'])

# Adding titles and labels
plt.title('Top 10 Traps with the Highest Average Daily Counts of Insects')
plt.xlabel('Trap Name')
plt.ylabel('Average Daily Counts')
plt.xticks(rotation=45)

# Displaying the plot
plt.tight_layout()
plt.show()