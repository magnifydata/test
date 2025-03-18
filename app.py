import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

try:
    df = pd.read_csv("data.csv")  # Load the CSV file into a DataFrame
    st.dataframe(df)
except FileNotFoundError:
    st.error("Error: data.csv not found.  Make sure it's in the same directory.")
