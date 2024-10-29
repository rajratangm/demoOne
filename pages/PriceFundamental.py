import streamlit as st 
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import plotly.graph_objects as go

st.header('Price and Fundamentals')


data = st.session_state.data


st.subheader('Original Data')
val= data.iloc[:, :-1]
st.dataframe(val)
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

    selected_date_range=st.slider('Select date range',min_value=datetime(2000, 1, 1), max_value=datetime(2024, 8, 31),value=(datetime(2000, 1, 1), datetime(2024, 8, 31)), format="YYYY-MM-DD")

    st.button('Refresh job list')



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


# def plot_graphs(filtered_data):
#     # Check if there is any data to plot
#     if filtered_data.empty:
#         st.warning("No data available for the selected filters.")
#         return
    
#     # Convert Date column to datetime if it isn’t already
#     if not pd.api.types.is_datetime64_any_dtype(filtered_data['Date']):
#         filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

#     # Create the plotly figure
#     fig = go.Figure()

#     # Add a line for each variable except the specified non-numeric columns
#     for column in filtered_data.columns:
#         if column not in ['Date', 'Job', 'Scenario', 'Area']:  # Skip non-numeric columns
#             fig.add_trace(go.Scatter(x=filtered_data['Date'], y=filtered_data[column],
#                                      mode='lines', name=column))

#     # Update layout for title, labels, and x-axis rotation
#     fig.update_layout(
#         title="Graphs of Different Variables Over Time",
#         xaxis_title="Date",
#         yaxis_title="Values",
#         xaxis=dict(tickangle=45),
#         legend_title="Variables",
#         template="plotly_white",
#         width=800,
#         height=500
#     )

#     # Display the plot in Streamlit
#     st.plotly_chart(fig)
# plot_graphs(filtered_data)


import streamlit as st
import pandas as pd
import plotly.graph_objects as go

def plot_graphs(filtered_data):
    # Check if there is any data to plot
    if filtered_data.empty:
        st.warning("No data available for the selected filters.")
        return
    
    # Convert Date column to datetime if it isn’t already
    if not pd.api.types.is_datetime64_any_dtype(filtered_data['Date']):
        filtered_data['Date'] = pd.to_datetime(filtered_data['Date'])

    # Loop through each column and plot individually
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
            st.plotly_chart(fig)

# Example of how to call the function with filtered data
plot_graphs(filtered_data)



