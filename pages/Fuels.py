import streamlit as st

# Set the page configuration
st.set_page_config(page_icon="🏭")

# Set the header
st.header('Generation')

# Initialize session state for selected option
if 'selected' not in st.session_state:
    st.session_state.selected = 'Generation by Unit'  # Set a default option

# Create buttons for navigation
# button_style = """
# <style>
#     .stButton > button {
#         font-size: 10px;
#         text-align: left;
#         margin-left: 0!important;
#         text-decoration: none;
#         border: none;  /* Remove default button border */
#         color: black;
#         padding: 5px 10px;  /* Adjust padding for closer spacing */
#         border-bottom: 3px solid grey;  /* Default grey underline */
#         border-radius: 0px;
#         background-color: transparent;  /* Transparent background */
#         width: 100%;  /* Full width for buttons */
#     }
#     .stButton > button:hover {
#         color: red;
#         border-bottom: 3px solid red;  /* Red underline on hover */
#     }
#     .stButton > button:focus {
#         outline: none;  /* Remove focus outline */
#     }
# </style>
# """
# st.markdown(button_style, unsafe_allow_html=True)

# Define button click behavior
if st.button("Generation Fuel1"):
    st.session_state.selected = "Generation by Unit"
elif st.button("Generation Fuel2"):
    st.session_state.selected = "Generation by Fuel"

# Display content based on selection
if st.session_state.selected == "Generation by Unit":
    st.write("Displaying data Fuels1")
elif st.session_state.selected == "Generation by Fuel":
    st.write("Displaying data Fuels2")
