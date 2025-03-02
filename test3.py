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

# Allow the user to select whether to combine all columns in one chart or not
combine_all = st.selectbox("Combine all columns in one chart?", options=["No", "Yes"])

# If the user selects "Yes" for combining all columns, plot all columns together
if combine_all == "Yes":
    if chart_type == "Line Chart":
        fig = px.line(df, x='Date', y=['Sales', 'Revenue', 'Profit'], title="Sales, Revenue, and Profit Over Time")
        fig.update_traces(line=dict(width=3))
        # Apply custom colors
        fig.update_traces(marker=dict(color=['blue', 'green', 'red']))
    elif chart_type == "Bar Chart":
        fig = px.bar(df, x='Date', y=['Sales', 'Revenue', 'Profit'], title="Sales, Revenue, and Profit Over Time (Bar Chart)")
        # Apply custom colors
        fig.update_traces(marker=dict(color=['blue', 'green', 'red']))
    st.plotly_chart(fig)

# If the user selects "No" for combining all columns, allow selection of one column to plot
else:
    column = st.selectbox("Select a data column to plot", options=['Sales', 'Revenue', 'Profit'])

    if chart_type == "Line Chart":
        fig = px.line(df, x='Date', y=column, title=f'{column} Over Time')
        fig.update_traces(line=dict(width=3))
        # Apply custom colors
        if column == 'Sales':
            fig.update_traces(marker=dict(color='blue'))
        elif column == 'Revenue':
            fig.update_traces(marker=dict(color='green'))
        elif column == 'Profit':
            fig.update_traces(marker=dict(color='red'))
    elif chart_type == "Bar Chart":
        fig = px.bar(df, x='Date', y=column, title=f'{column} Over Time (Bar Chart)')
        # Apply custom colors
        if column == 'Sales':
            fig.update_traces(marker=dict(color='blue'))
        elif column == 'Revenue':
            fig.update_traces(marker=dict(color='green'))
        elif column == 'Profit':
            fig.update_traces(marker=dict(color='red'))
    st.plotly_chart(fig)

# Add some additional explanation
st.write(f"Above is the chart showing the {column if combine_all == 'No' else 'Sales, Revenue, and Profit'} data.")
