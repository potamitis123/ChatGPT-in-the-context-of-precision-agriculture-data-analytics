# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 19:13:30 2023

@author: Ilyas Potamitis
"""

from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent

import pandas as pd

df = pd.read_csv('collective.csv')

# you need to have an API key. Note that the billing process of OPENAI's is indpendent of the ChatGPT billing.
openai_api_key = 'sk-3kz...'

chat = ChatOpenAI(openai_api_key = openai_api_key, model_name='gpt-4', temperature=0.0)
agent = create_pandas_dataframe_agent(chat, df, verbose=True)

p1 = "You are working with a pandas dataframe named 'df'. The column 'Counts' relates to insect captures."
p2 = "Column 'Temperature' relates to mean hourly temperature. "
p3 = "Column 'Humidity' relates to mean hourly humidity. "
p4 = "Column 'Lat' relates to the GPS coordinate latitude of the device. "
p5 = "Column 'Long' relates to the GPS coordinate Longitude of the device. "
p6 = "Column 'Name' relates to the name of the device."

prompt = p1 + p2 + p3 + p4 + p5 + p6

Q1 = "Which traps recorded the highest and lowest insect counts in an hour? In a day? What about in a week? Identify their location in each case"
Q2 = "Is there a significant difference in insect counts between adjacent (<1 km distance) traps?"
Q3 = "How does temperature vary across different traps? Pick five trap names at random and visualize this somehow and overlay a plot of min max values?"
Q4 = "Can you somehow quantify the correlation between temperature and humidity across all traps? Visualize for 2 traps."
Q5 = "Are there any trends or patterns in insect counts over time?"
Q6 = "What is the average daily count of insects for each trap? Visualize the first ten with the higher average value."
Q7 = "What time are the insects most active (circadian rhythm). Show a heatmap of activity where the y-axis is the hours of the day and x-axis the days. Present a colorbar."

CQ1 = "How many unique trap locations (Latitude, Longitude) are there? Can you show them on a world map?"
CQ2 = "How do counts vary with latitude and longitude in Greece only? Create a heatmap overlayed on a Greek map. Use folium"
CQ3 = "What is the average humidity and temperature and their standard deviation for the traps in Italy that captured weekly more than 100 insects in a week?"
CQ4 = "Create a list of events for the trap with ID 213 based on the timestamp between 21.00pm and 4am and counts that you believe are outliers. Focus on outliers with high values. Each hour should be treated independently. Plot the timeseries and mark on it the outlier values."
CQ5 = "Determine whether the traps with IDs 213 and 217 have similar catch patterns."
CQ6 = "Show a heatmap of Humidity and another one for temperature where the y-axis is the hours of the day and x-axis the timestamps. Visualize and present a colorbar that ranges from 0-100 for humidity and 0-60 for temperature."
CQ7 = "Find the closest three traps from the centre of the town Larissa. Perform crosscorrelation analysis on their counts."
CQ8 = "Is there a certain temperature and humidity threshold where the number of moths increases or decreases significantly?"
CQ9 = "Peak Activity: During which hours are the insects most active, and how does this relate to the prevailing temperature and humidity conditions?"

# Example call
agent.run(prompt + Q1)
