from streamlit_option_menu import option_menu
import streamlit as st 



selected = option_menu(
    menu_title=None,
    icons=['k','d','l','p','o'],
    options=['Fuel Option1','Fuel Option2','','',''], 
    orientation='horizontal',
    styles={
        "container":{'background-color':'white'},
        "text":{'color':'black'},
        'nav-link':{'border-bottom':'3px solid lightgray', 'color':'black', 'border-radius':'0px','text-size':'10px'},
        'nav-link-selected':{'border-bottom':'3px solid red', 'background-color':'white','text-size':'10px'},
        
        

    }
)

if selected=='Home':
    st.title('You have selected Home ')
if selected=='Projects':
    st.title('You have selected Projects')
if selected =='Contact':
    st.title('you have selected contacts')
