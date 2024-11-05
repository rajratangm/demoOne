
import streamlit as st

st.set_page_config(page_icon="🏭")
# Set the header
st.header('Generation')

# Initialize session state for selected option
if 'selected' not in st.session_state:
    st.session_state.selected = 'Generation by Unit'  # Set a default option

# Option menu for navigation with custom styles
selected = option_menu(
    None, 
    ["Generation by Unit", "Generation by Fuel",'',''],
    icons=['home', 'home','home', 'home'],  # Icons can be left empty if desired
    default_index=0,
    styles={
        "container": {
            "padding": "0!important",  # Remove padding around the container
            "background-color": "transparent",
            "border": "none",  # Remove default border
            "margi-left": "0!important",  # Remove margins to push closer to the left
            "width": "100%",  # Set width to 100% for full alignment
        },
        "nav-link": {
            "font-size": "10px", 
            "text-align": "left",  # Align text to the left
            "margin-left": "0!important",  # Remove margin to bring items closer
            "text-decoration": "none",  # Remove default underline
            "border-bottom": "3px solid grey",  # Default grey underline
            "color": "black",  # Text color
            "padding": "5px 10px",  # Adjust padding for closer spacing
            "border-radius": "0px",
        },
        "nav-link-selected": {
            "background-color": "transparent",  # Keep background transparent for selected
            "color": "red",  # Text color when selected
            "border-bottom": "3px solid red",  # Red underline for selected
            "border-radius": "0px",
        },
        "nav-link:hover": {
            "color": "red",
            "border-bottom": "3px solid red",  # Red underline on hover
        },
    },
    orientation='horizontal'
)

# Update selected link based on user interaction
st.session_state.selected = selected

# Render the selected page content
st.title(st.session_state.selected)

if st.session_state.selected == 'Generation by Unit':
    st.write("Content for Generation by Unit goes here.")
elif st.session_state.selected == 'Generation by Fuel':
    st.write("Content for Generation by Fuel goes here.")
