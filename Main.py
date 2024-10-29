import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit as st
st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "This is a custom about section."})

start_date = datetime(2000, 1, 1)
end_date = datetime(2024, 1, 8)  # You can adjust this to include more days
scenarios = ['Scenario_A', 'Scenario_B']
methods = ['TKO', 'SYS',
'HKD,'
'CHB',
'HKR',
'KNS',
'CGK']
data_length = 100  


dates = []
names = []
scenarios_list = []
methods_list = []
values1 = []
values2 = []


for i in range(data_length):
    current_date = start_date + timedelta(days=i // 4)  
    if i < 50:  
        name = 'BC_Jan22_Aug24_G6WithRe...'
    else:  
        name = 'BC_Jan22_Aug24_G6WithRe'
    
  
    scenario = scenarios[i % 2]
    method = methods[i % 2]
    
    
    value1 = round(45 + i * 0.5, 8)  
    value2 = round(np.random.uniform(0, 1000), 8) 

   
    dates.append(current_date.strftime('%m-%d-%Y'))
    names.append(name)
    scenarios_list.append(scenario)
    methods_list.append(method)
    values1.append(value1)
    values2.append(value2)


df = pd.DataFrame({
    'Date': dates,
    'Job': names,
    'Scenario': scenarios_list,
    'Area': methods_list,
    'Price': values1,
    'FundamentalValues': values2
})



##--------------------------------------------------------------------------------------------------------------
# Note:- for now a random data genration code is used this can be changed for API or csv with simple modifications code will not change much
# FOR CSV:-
# pd.read_csv('small_sample.csv')
# FOR API:-
#def fetch_data(api_url):
    # try:
    #     response = requests.get(api_url)
    #     response.raise_for_status()  # Raise an error for bad responses
    #     return response.json()  # Return the JSON data
    # except requests.exceptions.RequestException as e:
    #     st.error(f"Error fetching data: {e}")
    #     return None
##-----------------------------------------------------------------------------------------------------------------
st.session_state.data =  df





# for now stationary icons are used but later it will be replcaed by Streamlit Icon codes
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
