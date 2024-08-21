import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd


st.set_page_config(page_title="Redbus_streamlit", layout="wide")
st.write("DETAILS OF THE BUS ROUTES")


with st.sidebar:
    st.sidebar.image("images.png", use_column_width=True)
    menu = option_menu(
        menu_title="Main Menu",
        options=["Bus Routes"],
        styles={"nav-link-selected": {"background-color": "red"}}
    )

if menu == "Bus Routes":
    # List of encodings to try
    encodings = ['latin1', 'ISO-8859-1', 'windows-1252', 'utf-16']
    
    df = pd.DataFrame()  # Initialize an empty DataFrame
    for encoding in encodings:
        try:
            
            a = pd.read_csv("C:/Users/kanith1234/Downloads/redbus/AllRoutes.csv", encoding=encoding)
            columns = ["Name", "DeparturePoint", "Duration", "DepartureTime", "ArrivalTime", "Price", "SeatsAvailable", "Ratings"]
            df = pd.DataFrame(a, columns=columns)
            
            break
        
        except UnicodeDecodeError as e:
            st.write(f"UnicodeDecodeError with encoding '{encoding}': {e}")
            
    st.dataframe(df)
