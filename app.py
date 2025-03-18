import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit App")

try:
    df = pd.read_csv("data.csv")

    # Scatter plot of Age vs. another numerical column (replace 'Salary' with your column)
    fig = px.scatter(df, x="Age", y="Salary", title="Age vs. Salary")
    st.plotly_chart(fig)

except FileNotFoundError:
    st.error("Error: data.csv not found.")
