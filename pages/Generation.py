from streamlit_option_menu import option_menu
import streamlit as st 


st.title('Generation')
selected = option_menu(
    menu_title=None,
    icons=['k','d','l','t','tr'],
    options=['option1','option2','','',], 
    orientation='horizontal',
    styles={
        "container":{'background-color':'white'},
        "text":{'color':'black'},
        'nav-link':{'border-bottom':'3px solid lightgray', 'color':'black', 'border-radius':'0px', 'flex':'1'},
        'nav-link-selected':{'border-bottom':'3px solid red', 'background-color':'white'},
        
        

    }
)

if selected=='Generation option1':
    st.title('You have selected Home ')
    st.checkbox('show all options')
if selected=='Generation option2':
    st.title('You have selected Projects')

