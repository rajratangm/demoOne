from streamlit_option_menu import option_menu
import streamlit as st 


col1, col2, col3 = st.columns(3)
selected = option_menu(
    menu_title=None,
    icons=['k','d','l','t','tr'],
    options=['Generation option1','Generation option2','','',], 
    orientation='horizontal',
    styles={
        "container":{'background-color':'white','display':'flex','justify-content':'flex-start','weight':'100px'},
        "text":{'color':'black'},
        'nav-link':{'border-bottom':'3px solid lightgray', 'color':'black', 'border-radius':'0px'},
        'nav-link-selected':{'border-bottom':'3px solid red', 'background-color':'white'},
        'nav-link-contact':{'margin-right':'auto','padding-rght':'50px'}
        

    }
)

if selected=='Generation option1':
    st.title('You have selected Home ')
    st.checkbox('show all options')
if selected=='Generation option2':
    st.title('You have selected Projects')

