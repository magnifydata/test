import pandas as pd
import streamlit as st

# Load data from a CSV file
data = pd.read_csv("my_data.csv")  # Replace "my_data.csv" with your file

st.dataframe(data)  # Display the DataFrame in Streamlit
