"""
Code author:- Mainuddin Alam Irteja

Source of data information and citation:-
Published by: December 2023. Coastal Ecosystems Science Division, Maritimes region, Fisheries and Oceans Canada, Dartmouth NS. Link to dataset: https://open.canada.ca/data/en/dataset/dbbcb23a-d018-4b70-b8ec-89997aded770
Jeffery, N.W., Pettitt-Wade, H., Van Wyngaarden, M., and Stanley, R.R.E. Maritimes Coastal Biodiversity Monitoring Program – Beach Seining.
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
            "<h1 style='text-align: center;'>🐟 Coastal Diversity Dashboard 🐟</h1>", 
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
        st.info(
            "The project explores the coastal diversity of caught fish across different sites and seasons. "
            "By visualizing the data using charts and performing statistical analysis, this project tries to gain various insights about the data."
    )
    with st.container():
        st.subheader("Developer Information")
        st.info(
            "My name is Mainuddin Alam Irteja, the creator of this project. "
            "I'm passionate about ocean data, and this is my first project with it. "
            "Thank you for exploring this project!"
        )
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
    # Add the overview and gratitude for the data source
    with st.container():
        st.subheader("Overview")
        st.info(
            """
            This section provides information about the data source used in this project. 
            Special thanks and gratitude go to the data providers, without whom this project 
            would not have been possible.
            """
        )
    # Add a clickable link to the data source
    with st.container():
        st.subheader("Data Source Information and Citation")
        st.info("Published by: December 2023. Coastal Ecosystems Science Division, Maritimes region, Fisheries and Oceans Canada, Dartmouth NS. Link to dataset: [Click here](https://open.canada.ca/data/en/dataset/dbbcb23a-d018-4b70-b8ec-89997aded770).")
        st.info("Jeffery, N.W., Pettitt-Wade, H., Van Wyngaarden, M., and Stanley, R.R.E. Maritimes Coastal Biodiversity Monitoring Program – Beach Seining.")
    # Display the original dataset
    with st.container():
        st.subheader("The Original Data")
        st.dataframe(get_data, use_container_width=True)



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
    





