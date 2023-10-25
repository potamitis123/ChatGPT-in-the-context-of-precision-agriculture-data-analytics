# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: user
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

# Load the dataset
file_path = 'collective.csv'
data = pd.read_csv(file_path)

# Filtering data for trap IDs 213 and 217
data_213 = data[data['Name'] == 213].copy()
data_217 = data[data['Name'] == 217].copy()

# Merging data on Timestamp for comparison
merged_data = pd.merge(data_213, data_217, on='Timestamp', suffixes=('_213', '_217'))

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(merged_data['Timestamp'], merged_data['Counts_213'], label='Trap 213', alpha=0.7)
plt.plot(merged_data['Timestamp'], merged_data['Counts_217'], label='Trap 217', alpha=0.7)
plt.title('Insect Counts Comparison between Trap 213 and Trap 217')
plt.xlabel('Timestamp')
plt.ylabel('Counts')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculating the correlation between the counts in traps 213 and 217
correlation = merged_data['Counts_213'].corr(merged_data['Counts_217'])

correlation

# Two-sample t-test
t_stat, p_value = ttest_ind(merged_data['Counts_213'], merged_data['Counts_217'], equal_var=False)

# Function to calculate the FFT and frequencies
def calculate_fft(signal):
    N = len(signal)
    fft_values = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(N)
    return frequencies, np.abs(fft_values)

# Calculating FFT for traps 213 and 217
frequencies_213, fft_values_213 = calculate_fft(merged_data['Counts_213'])
frequencies_217, fft_values_217 = calculate_fft(merged_data['Counts_217'])

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(frequencies_213, fft_values_213, label='Trap 213')
plt.plot(frequencies_217, fft_values_217, label='Trap 217')
plt.title('Frequency Components of Insect Counts')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.legend()
plt.xlim(0, 0.1)  # Limiting the x-axis to show only low frequencies
plt.grid(True)
plt.tight_layout()
plt.show()

# Printing the t-test results
print(f"T-Statistic: {t_stat}, P-Value: {p_value}")
