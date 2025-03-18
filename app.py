import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

try:
    df = pd.read_csv("data.csv")

    # Create a selectbox to choose a name
    selected_name = st.selectbox("Select a Name:", df["Name"].unique())

    # Filter the DataFrame based on the selected name
    selected_row = df[df["Name"] == selected_name]

    # Display the selected row
    st.write("Selected Row:")
    st.dataframe(selected_row)
except FileNotFoundError:
    st.error("Error: data.csv not found.")
