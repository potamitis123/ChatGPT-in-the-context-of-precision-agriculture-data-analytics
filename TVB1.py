# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:17:53 2023

@author: ChatGPT
"""

import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram, welch
import numpy as np

# The same code can be used for the mosquito example as well

# Since the audio is in mp3 format, we need to convert it to wav format first
import pydub

# Load the mp3 file
audio = pydub.AudioSegment.from_mp3("treevibe.mp3")

# Export the audio to wav format
audio.export("treevibe.wav", format="wav")

# Read the wav file
sampling_rate, data = wavfile.read("treevibe.wav")

# If the audio is stereo, get one of the channels
if len(data.shape) == 2:
    data = data[:, 0]

# Plot the waveform in the time domain
time_points = np.arange(data.shape[0]) / sampling_rate
plt.figure(figsize=(10, 4))
plt.plot(time_points, data)
plt.title('Waveform in Time Domain')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()


# Calculate the Power Spectral Density (PSD)
frequencies, psd = welch(data, fs=sampling_rate, nperseg=1024)

# Plotting the PSD
plt.figure(figsize=(10, 4))
plt.semilogy(frequencies, psd)
plt.title('Power Spectral Density (PSD)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power/Frequency (dB/Hz)')
plt.grid()
plt.show()


# Calculate the spectrogram
frequencies_spec, times_spec, Sxx = spectrogram(data, fs=sampling_rate, nperseg=1024)

# Plotting the spectrogram
plt.figure(figsize=(10, 4))
plt.pcolormesh(times_spec, frequencies_spec, 10 * np.log10(Sxx), shading='gouraud')
plt.title('Spectrogram')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='Intensity (dB)')
plt.show()
