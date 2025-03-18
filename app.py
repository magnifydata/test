import streamlit as st
import pandas as pd
import plotly.express as px  # Recommended for interactive charts

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

try:
    df = pd.read_csv("data.csv")
    st.dataframe(df)

    # Create a bar chart of ages
    fig = px.bar(df, x="Name", y="Age", title="Age Distribution")
    st.plotly_chart(fig)  # Display the Plotly chart
except FileNotFoundError:
    st.error("Error: data.csv not found.")
