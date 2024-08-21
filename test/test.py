import Streamlit.streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title= "Sample App", layout= "wide")
st.write("This is my page context")


with st.sidebar:
    
    st.sidebar.image("img.jpeg", use_column_width= True)
    
    menu = option_menu(
    
                menu_title = "Select Any Menu",
                options = ["Data", "Plots", "Prediction"],
                styles = {
                    "nav-link-selected": {"background-color": "green"}
                }
    )
    
    

if menu == "Data":
    
    st.write("You seleted Data")
    
    
    data = pd.read_csv("data.csv")
    
    c1, c2, c3,c4,c5,c6,c7,c8,c9 = st.columns(9)
    
    with c1:
        selected_columns = st.multiselect("select any columns",data.columns)
    with c2:
        selected_edu = st.selectbox("select Education",data['Education'].unique())
    
    st.table(data[data['Education'].isin([selected_edu])][selected_columns])   # data[data['Education'] == "Masters"][['Age', "city", "Edcation"]]
    
    
if menu == "Plots":
    
    st.write("You seleted Plots")
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        
        a = st.text_input("Enter Your Name: ")
    with c2:
        b = st.number_input("Enter Age: ")
    with c3: 
        c = st.date_input(" DOB ")
    with c4: 
        d = st.selectbox("Gender ", ['Male', "Female"])
    
    st.write(a,b,c,d)
    

if menu == "Prediction":
    
    st.write("You seleted Prediction")
    
    a = [10, 13, 15, 16, 12, 23, 45, 16]
    
    fig = go.Figure(data= go.Pie(values = a)
                   
                   
                   )
    st.plotly_chart(fig)
    

# To run -> streamlit run file_name.py