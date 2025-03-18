import streamlit as st

st.title("Hello, Streamlit!")

st.write("This is a very simple Streamlit app.")

# Add a simple data display (using a dictionary)
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 28]}
st.write(data)
