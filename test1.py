import streamlit as st

# Set the title of the app
st.title("Welcome to My Streamlit App")

# Display some styled text
st.markdown("""
    <style>
    .big-font {
        font-size: 30px;
        color: #4CAF50;
        font-weight: bold;
    }
    </style>
    <p class="big-font">Hello, this is my first Streamlit app with custom styling!</p>
""", unsafe_allow_html=True)

# Add some additional content
st.write("Streamlit is an amazing framework for building web apps in Python!")
st.write("You can add widgets, charts, and much more with just a few lines of code.")
