import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Create a dummy dataset
# @st.cache_data
# def create_dummy_dataset(start_date='2000-01-01', end_date='2024-12-31'):
#     # Generate date range
#     date_range = pd.date_range(start=start_date, end=end_date, freq='D')

#     # Create dummy data
#     jobs = ['BC_Jan22_Aug24_G6WithRe...', 'BC_Jan22_Aug24_G6WithRe', 'BC_Jan22_Aug24_G6WithRe']
#     scenarios = ['Scenario_A', 'Scenario_B', 'Scenario_C']
#     areas = ['TKO', 'SYS', 'HKD', 'CHB', 'HKR', 'KNS', 'CGK']
    
#     # Create a grid of combinations for jobs, scenarios, and areas
#     combinations = pd.MultiIndex.from_product(
#         [date_range, jobs, scenarios, areas],
#         names=['Date', 'Job', 'Scenario', 'Area']
#     )

#     # Calculate the length of the combinations
#     num_combinations = len(combinations)

#     # Randomly generate Price and Fundamental Metric for each combination
#     prices = np.random.rand(num_combinations) * 100  # Random prices between 0 and 100
#     fundamental_metrics = np.random.rand(num_combinations) * 1000  # Random metric values

#     # Create DataFrame
#     df = pd.DataFrame({
#         'Date': combinations.get_level_values('Date'),
#         'Job': combinations.get_level_values('Job'),
#         'Scenario': combinations.get_level_values('Scenario'),
#         'Area': combinations.get_level_values('Area'),
#         'Price': prices,
#         'Fundamental Metric': fundamental_metrics
#     })
#     df.to_csv('sample.csv')

#     return df

# create_dummy_dataset()
st.session_state.data = pd.read_csv('small_sample.csv')



home = st.Page(
    page = 'pages/Home.py',
    title='🏠 Home ',
)

priceFundamental = st.Page(
    page = 'pages/PriceFundamental.py',
    title= ' 🗾 Price and Fundamental data'
)

Generation = st.Page(
    page = 'pages/Generation.py',
    title='🏭 Generation'
)

LoadFactors = st.Page(
    page = 'pages/LoadFactor.py',
    title= '💡 Load Factors'
)
Flows = st.Page(
    page = 'pages/Flows.py',
    title= '↔️ Flows'
)
Fuels = st.Page(
    page = 'pages/Fuels.py',
    title= '🚢 Fuels'
)
SubmitRuns = st.Page(
    page = 'pages/SubmitRuns.py',
    title= '📥 Submit runs'
)

CalndarCreation = st.Page(
    page = 'pages/CalenderCreation.py',
    title= '	📆 Calendar Creation'
)

Calibration = st.Page(
    page = 'pages/Calibration.py',
    title= '🔌 Calibration'
)

WeatherPaths = st.Page(
    page = 'pages/WeatherPaths.py',
    title= '💡 Weather Paths'
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
