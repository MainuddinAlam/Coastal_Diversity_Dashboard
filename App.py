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
    st.set_page_config(page_title="Research of Coastal Diversity")
    st.title("Research of Coastal Diversity")
    st.write("")

# Function to read and return the given data file
def read_csv_file():
    return pd.read_csv("./datas/SeineCatch.csv")

# Function to display the home section
def home_section():
    st.header("Overview")
    st.write("Welcome to the Home section.")

# Function to display the analysis section
def analysis_section():
    st.header("Analysis")
    st.write("This is the Analysis section.")

# Function to display the summary section
def summary_section():
    st.header("Summary")
    st.write("This is the summary section.")

# Function to display the project information
def information_section():
    st.header("Project information")
    st.write("This section includes information about the data source.")
    st.write(" This section also includes the github repository of this project")



# Get the data
get_data = read_csv_file()

# Set the title and tab name
set_Initial()

# Creating the navigation bar and making it functional
tabs = st.tabs(["Home", "Analysis", "Summary", "Project information"])
with tabs[0]:
    home_section()          # Display the home section
with tabs[1]:
    analysis_section()      # Display the analysis section
with tabs[2]:
    summary_section()       # Display the summary section
with tabs[3]:
    information_section()   # Display the project information section
    





