from streamlit_option_menu import option_menu
import streamlit as st 


st.title('Fuel')
selected = option_menu(
    menu_title=None,
    icons=['k','d','l','kp'],
    options=['Fuel Option1','Fuel Option2','',''], 
    orientation='horizontal',
    styles={
        "container":{'background-color':'white','display':'flex','justify-content':'flex-start','weight':'100px'},
        "text":{'color':'black'},
        'nav-link':{'border-bottom':'3px solid lightgray', 'color':'black', 'border-radius':'0px'},
        'nav-link-selected':{'border-bottom':'3px solid red', 'background-color':'white',},
        'nav-link-contact':{'margin-right':'auto','padding-rght':'50px'}
        

    }
)

if selected=='Fuel Option1':
    st.title('You have selected Fuel Option1 ')
if selected=='Fuel Option2':
    st.title('You have selected Fuel Option2')

