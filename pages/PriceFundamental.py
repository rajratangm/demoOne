import streamlit as st 
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt

st.set_page_config(page_icon="🗾", page_title='PriceFundamental')

st.header('Price and Fundamentals')


data = st.session_state.data

st.subheader('Original Data')

val= data.iloc[:, :-1]
st.dataframe(val,use_container_width=True)

data['Date'] = pd.to_datetime(data['Date'])

with st.sidebar:
    st.header('Select data')
    st.write('Use the widget belo to explore the generation model')

    st.subheader('Select job')

    st.checkbox('Show inputs only', help="Check to show only the imputs for the run. This is useful if the ruin hasn't been solved and inserted yet. If results are not needed, this can be checked to avoid loading the results")
    
    selected_job = st.selectbox('Select a job', ['BC_Jan22_Aug24_G6WithRe...','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe','BC_Jan22_Aug24_G6WithRe'])
    selected_scenario= st.selectbox('Select Scenarios',['Scenario_A','Scenario_B'])

    st.checkbox('Compare two jobs', help='compare jobs here')
    st.checkbox('Select all areas',help='select all areas here')

    selected_areas= st.multiselect('Select areas',['TKO','SYS','HKD','CHB','HKR','KNS','CGK'], default='TKO')

    st.selectbox('Select granual', ['Hourly','Daily','Weekly','Monthly','Quarterly','Yearly'])

    st.button('Load Data')

    selected_date_range=st.slider('Select date range',min_value=datetime(2024, 1, 1), max_value=datetime(2024, 8, 31),value=(datetime(2024, 1, 1), datetime(2024, 8, 31)), format="YYYY-MM-DD")

    st.button('Refresh job list')


data = st.session_state.data
st.subheader('Original Data')
st.dataframe(data)
data['Date'] = pd.to_datetime(data['Date'])

filtered_data = data[
    (data['Job'] == selected_job) &
    (data['Scenario'] == selected_scenario) &
    (data['Area'].isin(selected_areas)) &
    (data['Date'] >= selected_date_range[0]) &
    (data['Date'] <= selected_date_range[1])
]

# Display the filtered DataFrame
st.subheader('Filtered Data')
fVal = filtered_data.iloc[:, :-1]
st.dataframe(fVal, use_container_width=True)


def plot_graphs(filtered_data):
    # Check if there is any data to plot
    if filtered_data.empty:
        st.warning("No data available for the selected filters.")
        return
    
    # Set the figure size
    plt.figure(figsize=(12, 6))
    
    # Plotting each variable over time
    for column in filtered_data.columns:
        if column not in ['Date', 'Job', 'Scenario', 'Area']:  # Skip non-numeric columns
            fig = go.Figure()
            
            # Create line plot for the specific column
            fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data[column],
                                     mode='lines', name=column))

            # Update layout for each plot
            fig.update_layout(
                title=f"Graph of {column} Over Time",
                xaxis_title="Date",
                yaxis_title=column,
                xaxis=dict(tickangle=45),
                template="plotly_white",
                width=800,
                height=400
            )
            
            # Display each plot in Streamlit
            st.plotly_chart(fig,use_container_width=True)

plot_graphs(filtered_data)
