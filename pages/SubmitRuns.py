import streamlit as st 


st.set_page_config(page_icon="📥", layout='wide')
st.title('Run creator')

col1, col2 = st.columns(2)

with col1:
    st.checkbox('Backtest run', help='To check back test')
    st.date_input('Start date', help='Start date')
    st.date_input('End date', help='End date')

with col2: 
    st.checkbox('Fix flows')
    st.number_input('Number of scenarios', value=1, help='Number of scenarios', min_value=0)
    st.number_input('Number of hours to aggragate', min_value=0, help='Number of hours', value=6)

with col1:
    st.markdown('---')

    st.checkbox('Custom as of dates for weather scenarios', help='Custom as dates for weather scenarios')

    st.markdown('---')

    st.checkbox('Use a custom MasterGen file', help='Use a custom MasterGen file')

    st.button('Reset Job ID')

    st.text_input('Job ID', value='BC_2024-11-05_2024-11-05_G0_20241105054433')

    st.checkbox('Insert data in the DB', help='Insert data in the DB')

    st.selectbox('Select granularity', options=('Weekly','Hourly','Daily'), help='Select granularity', )

    st.button('Create inputs only')
    st.button('Run model optimisation')
st.dataframe(st.session_state.data, use_container_width=True)
st.button('Refresh jobs')
st.checkbox('Display tasks', help='Display tasks')

st.header('Enable/disable a run')
st.markdown('---')
st.selectbox('Select a job ID to enable/diable', options=['job1', 'job2','job3'])
st.button('Enable/Diable run for UI')
