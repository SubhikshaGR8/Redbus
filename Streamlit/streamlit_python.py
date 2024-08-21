import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import re


st.set_page_config(page_title= "Redbus_streamlit", layout= "wide")
st.write("DETAILS OF THE BUS ROUTES")




with st.sidebar:
    
    st.sidebar.image("images.png", use_column_width= True)
    
    menu = option_menu(menu_title = "Main Menu",
                       options = ["Bus Routes"],
                       styles = {"nav-link-selected": {"background-color": "red"}})
    

if menu == "Bus Routes":
    try:
        a = pd.read_csv("C:/Users/kanith1234/Downloads/redbus/AllRoutes.csv", encoding='latin1') # csv
        columns =["Name","DepaturePoint","Duration","DepatureTime","ArrivalTime","Price","Seat Available","Ratings"]
        df = pd.DataFrame(a, columns=columns)
    except UnicodeDecodeError as e:
        st.write(f"UnicodeDecodeError: {e}")
        df=pd.DataFrame()
    st.dataframe(df)

       








