import streamlit as st
import pandas as pd
import plotly.express as px

# Create some sample data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Sales': [150, 200, 180, 220, 250, 270, 300, 310, 350, 400],
    'Revenue': [1000, 1200, 1100, 1300, 1400, 1600, 1800, 1900, 2100, 2300],
    'Profit': [500, 600, 550, 650, 700, 750, 800, 850, 900, 950]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Set the title of the app
st.title("Interactive Chart with Plotly")

# Display the DataFrame to the user
st.write("Here is the sample data:")
st.write(df)

# Allow the user to select a chart type
chart_type = st.selectbox("Select a chart type", options=["Line Chart", "Bar Chart"])

# Allow the user to select a column to plot
column = st.selectbox("Select a data column to plot", options=['Sales', 'Revenue', 'Profit'])

# Create the interactive plot based on the selected chart type
if chart_type == "Line Chart":
    # Line chart
    fig = px.line(df, x='Date', y=column, title=f'{column} Over Time')
    st.plotly_chart(fig)
elif chart_type == "Bar Chart":
    # Bar chart
    fig = px.bar(df, x='Date', y=column, title=f'{column} Over Time (Bar Chart)')
    st.plotly_chart(fig)

# Add some additional explanation
st.write(f"Above is the chart showing the {column} data over the days.")
