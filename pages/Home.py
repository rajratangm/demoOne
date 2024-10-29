import streamlit as st 
# st.set_page_config(page_title="My Streamlit App", page_icon=":sparkles:", layout="wide", initial_sidebar_state="expanded", menu_items={"About": "This is a custom about section."})


image_url = "data:image/jpeg;base64,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"

# Display the online image
st.image(image_url,)


st.markdown("""


0
Generation Model UI ⚡
Welcome to the Generation Model UI! 👋 This app enables the user to analyse results generated with the Generation Model, as well as to launch runs.
The app is divided into several sections, each of which focuses on a different aspect of the model:

Generation Model: This section allows the user to analyse results generated with the Generation Model and to launch runs.

Price and Fundamental Data: This page allows the user to analyse price and fundamental data.
Generation: This page allows the user to analyse generation data.
Load Factors: This page allows the user to analyse load factors.
Flows: This page allows the user to analyse flows.
Fuel Prices: This page allows the user to analyse fuel prices.
Submit runs: This page allows the user to submit runs to be solved by the Generation Model and using custom parameters. It also allows the user to control the progress of existing runs.
Weather Scenarios: This page allows the user to analyse and launch weather scenarios generation (Load, Solar, Wind,..).

Load Forecast - Calendar Creation: This page allows the user to create a calendar for a load forecast.
Load Forecast - Calibration: This page allows the user to change parameters and calibrate the load forecast model.
Load Forecast - Weather Paths: This page allows the user to execute a forecast for specified area. (Pages to be added: Solar and Wind scenarios)
Commodities scenarios: This page allows the user to analyse and launch commodities scenarios generation. This includes the fuel indexes prices to be used in the Generation Model. (Section to be impemented)

⏲️
Click here to add/modified scheduled jobs using Azure Logic Apps.

👾
Useful links for developers:

Generation model UI - repository (JapanGenerationModelUI) and app
Backend web app - repository (generation-model-backend-app) and app
Input generation app - repository (generation-model-inputs-app) and app (generation-model-inputs-app)
Generation model batch service - repository (JapanGenerationModelDocker) and app - generationmodelbatch
Input generation package - repository (GenerationModelInputs)
Supply and demand model package - repository (Japan_GenerationModel)
Generation Model - System Overview

0



""" )




# st.write(st.session_state.description.DESCR)
