import streamlit as st
import pandas as pd
import numpy as np

# Create a dataset with 500 rows, realistic date variability, and specified areas
def create_dummy_dataset():
    # Starting date and range to cover a few months with spaced intervals
    start_date = pd.to_datetime('2024-01-01')
    date_list = [start_date + pd.Timedelta(days=int(i)) for i in np.cumsum(np.random.randint(1, 5, size=125))]
    
    # Repeat dates to create 500 rows
    dates = date_list * (500 // len(date_list) + 1)
    dates = dates[:500]  # Limit to exactly 500 rows

    jobs = ['BC_Jan22_Aug24_G6WithRe...', 'BC_Jan22_Aug24_G6WithRe']
    scenarios = ['Scenario_A', 'Scenario_B']
    areas = ['TKO', 'SYS', 'HKD', 'CHB', 'HKR', 'KNS', 'CGK']  # Updated areas list

    # Expand jobs, scenarios, and areas to cover 500 entries
    jobs_repeated = np.random.choice(jobs, size=500)
    scenarios_repeated = np.random.choice(scenarios, size=500)
    areas_repeated = np.random.choice(areas, size=500)
    
    # Generate prices and fundamental metrics
    prices = np.random.rand(500) * 100
    fundamental_metrics = np.random.rand(500) * 1000

    # Create DataFrame
    df = pd.DataFrame({
        'Date': dates,
        'Job': jobs_repeated,
        'Scenario': scenarios_repeated,
        'Area': areas_repeated,
        'Price': prices,
        'Fundamental Metric': fundamental_metrics
    })
    
    return df

# Create the dataset
data = create_dummy_dataset()

# Display the dataset in Streamlit
data.to_csv('sample.csv')
