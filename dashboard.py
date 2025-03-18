import streamlit as st

st.title("My First Dashboard")
st.write("Hello, world! This is a simple Streamlit app.")

# Add a simple data display
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
st.write(data)  # Streamlit can display dictionaries, DataFrames, etc.
