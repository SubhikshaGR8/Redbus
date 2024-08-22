import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from datetime import time


# Set up the Streamlit page configuration
st.set_page_config(page_title="Redbus_streamlit", page_icon='📊', layout="wide")
st.write("<h1 style='color: red;'> DETAILS OF THE BUS ROUTES</h1>",unsafe_allow_html=True)


with st.sidebar: 
    st.sidebar.image("images.png", use_column_width= True)
    menu = option_menu(menu_title = "Main Menu",
                       options = ["Search Buses","View Buses"],
                       styles = {"nav-link-selected": {"background-color": "red"}}
                       )
    


if menu == "Search Buses":
    # List of encodings to try
    encodings = ['latin1', 'ISO-8859-1', 'windows-1252']
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        option = st.selectbox(
        " ",
        ("West Bengal Transport Corporation", "Bihar State Road Transport(BSRTC)", "NORTH BENGAL STATE TRANSPORT", "WBTC (CTC)","BSRTC","South Bengal State Transport(SBSTC)","PEPSU (Punjab)","PEPSU (Punjab) 2", "Rajasthan State Transport", "Haryana State Transport", "Utthar Pradesh State Transport", "Chandigarh Transport Undertaking (CTU)", "KSRTC (Kerala)", "Kadamba Transport Corporation Limited (KTCL)", "Telungana SRTC", "Andra Pradesh SRTC","Assam State Transport Corporation (ASTC)", "KAAC TRANSPORT", "Sikkim Nationalised Transport (SNT)","Meghalaya Transport Corporation(MTC)"),
        index=None,
        placeholder="Select A Bus Route...",
        )
        st.write("You selected:", option) 
        if option=="West Bengal Transport Corporation": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/1-West Bengal Transport Corporation/route.csv"
        elif option=="Bihar State Road Transport(BSRTC)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/2-Bihar State Road Transport Corporation (BSRTC)/route.csv"
        elif option=="NORTH BENGAL STATE TRANSPORT": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/3-NORTH BENGAL STATE TRANSPORT CORPORATION/route.csv"
        elif option=="WBTC (CTC)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/4-WBTC (CTC)/route.csv"
        elif option=="BSRTC": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/5-BSRTC Operated By VIP Travels/route.csv"
        elif option=="South Bengal State Transport(SBSTC)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/6-South Bengal State Transport Corporation (SBSTC)/route.csv"
        elif option=="PEPSU (Punjab)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/8-PEPSU (Punjab)/route.csv"
        elif option=="PEPSU (Punjab) 2": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/9-PEPSU (Punjab)/route.csv"
        elif option=="Rajasthan State Transport": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/10-RSRTC/route.csv"
        elif option=="Haryana State Transport": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/11-HRTC/route.csv"
        elif option=="Utthar Pradesh State Transport": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/12-UPSRTC/route.csv"
        elif option=="Chandigarh Transport Undertaking (CTU)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/13-Chandigarh Transport Undertaking (CTU)/route.csv"
        elif option=="KSRTC (Kerala)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/16-KSRTC (Kerala)/route.csv"
        elif option=="Kadamba Transport Corporation Limited (KTCL)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/17-Kadamba Transport Corporation Limited (KTCL)/route.csv"
        elif option=="Telungana SRTC": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/18-TSRTC/route.csv"
        elif option=="Andra Pradesh SRTC": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/19-APSRTC/route.csv"
        elif option=="Assam State Transport Corporation (ASTC)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/20-Assam State Transport Corporation (ASTC)/route.csv"
        elif option=="KAAC TRANSPORT": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/21-KAAC TRANSPORT/route.csv"
        elif option=="Sikkim Nationalised Transport (SNT)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/22-Sikkim Nationalised Transport (SNT)/route.csv"
        elif option=="Meghalaya Transport Corporation(MTC)": 
            readCSv ="C:/Users/kanith1234/Downloads/redbus/bus/23-Meghalaya Transport Corporation(MTC)/route.csv"
        

        else:
            readCSv = "C:/Users/kanith1234/Downloads/redbus/AllRoutes.csv"

    with col2:
        option = st.selectbox(
            " ",
            ("Bangalore", "Kochi", "Chennai", "mumbai", "Kolkata", "Delhi"),
            index=None,
            placeholder="Select Your Source...",
        )
        st.write("You selected:", option)
    with col3:
        option = st.selectbox(
            " ",
            ("< 1000₹ 💵", "₹1000 💷 - ₹2000 💴", "> ₹2000💶"),
            index=None,
            placeholder="Select A Price range...",
        )
        st.write("You selected:", option) 
    with col4:
        option = st.selectbox(
            " ",
            ("⭐⭐⭐⭐⭐", "⭐⭐⭐⭐ ", "⭐⭐⭐ " ,"⭐⭐"),
            index=None,
            placeholder="Select A Rating...",
        )
        st.write("You selected:", option)

    
    
    
    df = pd.DataFrame()  
    successful = False  # Flag to check if reading was successful
    for encoding in encodings:
        try:
            df = pd.read_csv(f"{readCSv}", encoding=encoding)
            columns = ["name", "Routes", "Duration", "DepartureTime", "ArrivalTime", "Price", "SeatsAvailable", "Ratings"]

            # Check if DataFrame has the correct number of columns
            if len(df.columns) == len(columns):
                df.columns = columns  
                successful = True
                break  # BREAK SEI OR
        except UnicodeDecodeError as e:
            st.write(f"UnicodeDecodeError with encoding '{encoding}': {e}")
        except Exception as e:
            st.write(f"Error with encoding '{encoding}': {e}")
       
        
    edited_df = st.data_editor(
        df,
        width=1500,
        column_config={
            "name": st.column_config.TextColumn(
            "🚌 Bus Name",
            help="Bus Names 🚌",
            default="st.",
            max_chars=50,
            ),
            "Rating": st.column_config.NumberColumn(
                "Rating",
                help="Rating of the bus",
                min_value=1.000,
                max_value=5.000,
                step=0.100,
                format="%f ⭐",
            ),

        },
        disabled=["command", "is_widget"],
        hide_index=True,
    )

   


if menu == "View Buses":
    encodings = ['latin1', 'ISO-8859-1', 'windows-1252']
    df = pd.DataFrame()
    successful = False  # Flag to check if reading was successful
    for encoding in encodings:
        try:
            df = pd.read_csv("C:/Users/kanith1234/Downloads/redbus/AllRoutes.csv", encoding=encoding)
            columns = ["name", "Route", "Source", "Dest","Duration", "Starting time", "Reach Time","Price", "Seats", "Rating"]

            # Check if DataFrame has the correct number of columns
            if len(df.columns) == len(columns):
                df.columns = columns  
                successful = True
                break  # BREAK SEI OR
        except UnicodeDecodeError as e:
            st.write(f"UnicodeDecodeError with encoding '{encoding}': {e}")
        except Exception as e:
            st.write(f"Error with encoding '{encoding}': {e}")
    edited_df = st.data_editor(
        df,
        column_config={
            "Name": "Name",
            "Rating": st.column_config.NumberColumn(
                "Rating",
                help="Rating of the bus",
                width="medium",
                min_value=1.000,
                max_value=5,
                step=0.1,
                format="%d ⭐",
            ),

        },
        disabled=["command", "is_widget"],
        hide_index=True,
    )

       








