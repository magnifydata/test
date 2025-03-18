import streamlit as st
import pandas as pd

st.title("Streamlit App")

try:
    df = pd.read_csv("data.csv")

    # Multiselect widget for filtering by category (replace 'Category' with your column)
    selected_categories = st.multiselect(
        "Select Categories:", options=df["Category"].unique(), default=df["Category"].unique()
    )

    # Filter the DataFrame
    filtered_df = df[df["Category"].isin(selected_categories)]

    st.dataframe(filtered_df)

except FileNotFoundError:
    st.error("Error: data.csv not found.")
