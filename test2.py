import streamlit as st

# Set the title of the app
st.title("Personalized Greeting App")

# Ask for the user's name using a text input
name = st.text_input("What is your name?")

# Display a personalized greeting if the user enters a name
if name:
    st.markdown(f"""
        <style>
        .greeting {{
            font-size: 36px;
            color: #FF6347;
            font-weight: bold;
            text-align: center;
        }}
        </style>
        <p class="greeting">Hello, {name}! Welcome to my Streamlit app!</p>
    """, unsafe_allow_html=True)
else:
    st.write("Please enter your name to receive a greeting.")

# Add some additional content
st.write("Streamlit makes it easy to create interactive apps with Python.")
st.write("Try typing your name in the box above and see the greeting!")
