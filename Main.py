import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import config
import os 
import requests
# from streamlit_notification_center_component import notification_center


# Define the initial parameters
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 8)  # You can adjust this to include more days
scenarios = ['Scenario_A', 'Scenario_B']
methods = ['TKO', 'SYS']
data_length = 100  # Total number of rows needed

# Create lists to store generated data
dates = []
names = []
scenarios_list = []
methods_list = []
values1 = []
values2 = []

# Generate data
for i in range(data_length):
    current_date = start_date + timedelta(days=i // 4)  # Change every 4 entries
    if i < 50:  # For the first half
        name = 'BC_Jan22_Aug24_G6WithRe...'
    else:  # For the second half
        name = 'BC_Jan22_Aug24_G6WithRe'
    
    # Alternate scenarios and methods
    scenario = scenarios[i % 2]
    method = methods[i % 2]
    
    # Generate random float values
    value1 = round(45 + i * 0.5, 8)  # Just an example increment for values
    value2 = round(np.random.uniform(0, 1000), 8)  # Random value for the second column

    # Append generated data to lists
    dates.append(current_date.strftime('%m-%d-%Y'))
    names.append(name)
    scenarios_list.append(scenario)
    methods_list.append(method)
    values1.append(value1)
    values2.append(value2)

# Create a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Job': names,
    'Scenario': scenarios_list,
    'Area': methods_list,
    'Price': values1,
    'FundamentalValues': values2
})

# Display the DataFrame


# if config.API_KEY:
#     response = requests.get(config.API_KEY)
#     if(response.status==200):

# df = pd.DataFrame([])
st.session_state.data =  df


home = st.Page(
    page = 'pages/Home.py',
    title='Home ',
)

priceFundamental = st.Page(
    page = 'pages/PriceFundamental.py',
    title= ' Price and Fundamental data'
)

Generation = st.Page(
    page = 'pages/Generation.py',
    title='Generation'
)

LoadFactors = st.Page(
    page = 'pages/LoadFactor.py',
    title= 'Load Factors'
)
Flows = st.Page(
    page = 'pages/Flows.py',
    title= 'Flows'
)
Fuels = st.Page(
    page = 'pages/Fuels.py',
    title= 'Fuels'
)
SubmitRuns = st.Page(
    page = 'pages/SubmitRuns.py',
    title= 'Submit runs'
)

CalndarCreation = st.Page(
    page = 'pages/CalenderCreation.py',
    title= 'Calendar Creation'
)

Calibration = st.Page(
    page = 'pages/Calibration.py',
    title= 'Calibration'
)

WeatherPaths = st.Page(
    page = 'pages/WeatherPaths.py',
    title= 'Weather Paths'
)

pg = st.navigation(
   {
       'Home':[home],
       'Generation Model':[priceFundamental, Generation, LoadFactors, Flows, Fuels, SubmitRuns],
       'Load Scenarios': [CalndarCreation, Calibration, WeatherPaths],
       'Commodities scenarios':[]
   }
)

pg.run()
