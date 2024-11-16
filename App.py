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
    # Set the tab name and logo
    st.set_page_config(
        page_title="Coastal Diversity Dashboard",
        page_icon="🐟", 
    )
    # Set the title and logo
    with st.container():
        st.markdown(
            "<h1 style='text-align: center;'>Coastal Diversity Dashboard 🐟</h1>", 
            unsafe_allow_html=True
    )
    st.write("")

# Function to read and return the given data file
def read_csv_file():
    return pd.read_csv("./datas/SeineCatch.csv")

# Function to display the home section
def home_section():
    # Display the overview 
    with st.container():
        st.subheader("Overview")
        st.info("The project explores the coastal diversity of caught fish across different sites and seasons. By visualizing the data using charts and performing statistical analysis, this project tries to gain various insights about the data.")
    # Display the members
    with st.container():
        st.subheader("Members")
        st.info("My name is Mainuddin Alam Irteja, and I am the creator, and only member of this project.")
    # Add the github section
    with st.container():
        st.subheader("Github")
        st.info("The project is kept at Github. Click [Github repository](https://github.com/MainuddinAlam/Ocean_Of_Data).")


# Function to display the analysis section
def analysis_section():
    st.header("Analysis")
    st.write("This is the Analysis section.")

# Function to display the summary section
def summary_section():
    st.header("Summary")
    st.write("This is the summary section.")

# Function to display the data information
def information_section():
    st.header("Data information")
    st.write("This section includes information about the data source.")



# Get the data
get_data = read_csv_file()

# Set the title and tab name
set_Initial()

# Creating the navigation bar and making it functional
tabs = st.tabs(["Home", "Analysis", "Summary", "Data information"])
with tabs[0]:
    home_section()          # Display the home section
with tabs[1]:
    analysis_section()      # Display the analysis section
with tabs[2]:
    summary_section()       # Display the summary section
with tabs[3]:
    information_section()   # Display the data information section
    





