import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a small dummy dataset
def create_small_dummy_dataset():
    date_range = pd.date_range(start='2024-01-02', end='2024-01-03', freq='D')
    jobs = ['BC_Jan22_Aug24_G6WithRe...', 'BC_Jan22_Aug24_G6WithRe']
    scenarios = ['Scenario_A', 'Scenario_B']
    areas = ['TKO', 'SYS']
    
    combinations = pd.MultiIndex.from_product(
        [date_range, jobs, scenarios, areas],
        names=['Date', 'Job', 'Scenario', 'Area']
    )

    num_combinations = len(combinations)
    prices = np.random.rand(num_combinations) * 100
    fundamental_metrics = np.random.rand(num_combinations) * 1000

    df = pd.DataFrame({
        'Date': combinations.get_level_values('Date'),
        'Job': combinations.get_level_values('Job'),
        'Scenario': combinations.get_level_values('Scenario'),
        'Area': combinations.get_level_values('Area'),
        'Price': prices,
        'Fundamental Metric': fundamental_metrics
    })

    return df

# Create the small dataset
data = create_small_dummy_dataset()
