import streamlit as st
import pandas as pd

st.title("Hello, Streamlit!")

st.write("This is a very simple Streamlit app.")

# Add a simple data display (using a Pandas DataFrame)
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 28]}
df = pd.DataFrame(data)  # Convert the dictionary to a DataFrame
st.dataframe(df)  # Display the DataFrame
