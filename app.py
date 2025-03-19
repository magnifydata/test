import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Employee Data Filter")

try:
    df = pd.read_csv("data.csv")

    st.sidebar.header("Filter Options")

    # Multiselect widget for filtering by category (in the sidebar)
    selected_categories = st.sidebar.multiselect(
        "Select Employee Categories:",
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )

    # Slider for filtering by salary (in the sidebar)
    min_salary = float(df["Salary"].min())
    max_salary = float(df["Salary"].max())
    salary_range = st.sidebar.slider(
        "Select Salary Range ($):",
        min_value=min_salary,
        max_value=max_salary,
        value=(min_salary, max_salary),
    )

    # Filter the DataFrame
    filtered_df = df[df["Category"].isin(selected_categories)]
    filtered_df = filtered_df[
        (filtered_df["Salary"] >= salary_range[0]) & (filtered_df["Salary"] <= salary_range[1])
    ]

    # Calculate average salary per category for the filtered data
    avg_salary_per_category = filtered_df.groupby("Category")["Salary"].mean().reset_index()

    # Create the bar chart using plotly
    fig = px.bar(
        avg_salary_per_category,
        x="Category",
        y="Salary",
        labels={"Category": "Employee Category", "Salary": "Average Salary ($)"},
        title="Average Salary per Employee Category",
    )

    # Create two columns for layout (adjust the ratio)
    col1, col2 = st.columns([3, 2])  # DataFrame takes 3/5, graph takes 2/5

    with col1:
        st.header("Employee Information")
        st.dataframe(filtered_df)
        st.write(f"Number of results: {len(filtered_df)}")

    with col2:
        st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Error: data.csv not found.")
except KeyError as e:
    st.error(
        f"Error: Column '{e}' not found in data.csv.  Make sure 'Salary' and 'Category' columns exist."
    )
except ValueError:
    st.error(
        "Error: 'Salary' column contains non-numeric values. Please ensure it only contains numbers."
    )
