"""
Code author:- Mainuddin Alam Irteja

Source of data:- w
"""

# Import important modules needed for the application
import streamlit as st
import pandas as pd
import plotly as plt

# Function to set the title and tab name
def set_Initial():
    st.set_page_config(page_title="Coastal Diversity Research Dashboard")
    st.title("Coastal Diversity Research Dashboard")
    st.write("")

 

# Function to read the given data file
def read_csv_file():
    csv_path = "./datas/SeineCatch.csv"
    seine_catch_csv = pd.read_csv(csv_path)
    return seine_catch_csv
 
# Set the title and tab name
set_Initial()

# Get the data
get_data = read_csv_file()



# Sidebar menu with borderless buttons
st.sidebar.title("Table of Contents")
home_button = st.sidebar.button("1. Home")
about_button = st.sidebar.button("2. Overview")
contact_button = st.sidebar.button("3. Analysis")