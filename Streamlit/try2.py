import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Set up the Streamlit page configuration
st.set_page_config(page_title="Redbus_streamlit", layout="wide")
st.write("<h1 style='color: red;'> DETAILS OF THE BUS ROUTES</h1>",unsafe_allow_html=True)

# Sidebar for navigation
with st.sidebar:
    st.sidebar.image("images.png", use_column_width=True)
    menu = option_menu(
        menu_title="Main Menu",
        options=["Bus Routes"],
        styles={"nav-link-selected": {"background-color": "red"}}
    )

if menu == "Bus Routes":
    # List of encodings to try
    encodings = ['latin1', 'ISO-8859-1', 'windows-1252', 'utf-8', ]

    df = pd.DataFrame()  
    successful = False  # Flag to check if reading was successful

    for encoding in encodings:
        try:
            
            df = pd.read_csv("C:/Users/kanith1234/Downloads/redbus/AllRoutes.csv", encoding=encoding)
            
            columns = ["Name", "DeparturePoint", "Duration", "DepartureTime", "ArrivalTime", "Price", "SeatsAvailable", "Ratings"]
            
            # Check if DataFrame has the correct number of columns
            if len(df.columns) == len(columns):
                df.columns = columns  
                successful = True
                break  # BREAK SEI OR
            else:
                st.write(f"Column mismatch with encoding '{encoding}'")
        
        except UnicodeDecodeError as e:
            st.write(f"UnicodeDecodeError with encoding '{encoding}': {e}")
        except Exception as e:
            st.write(f"Error with encoding '{encoding}': {e}")


    
    st.dataframe(df)
