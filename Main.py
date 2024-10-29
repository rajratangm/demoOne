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

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

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


st.session_state.data =  df
# pd.read_csv('small_sample.csv')



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
