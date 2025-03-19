import streamlit as st
import pandas as pd

st.title("Employee Data Filter")  # Improved app title

try:
    df = pd.read_csv("data.csv")

    st.header("Filter Employee Information") #Added header

    # Multiselect widget for filtering by category
    selected_categories = st.multiselect(
        "Select Employee Categories:",  # Improved label
        options=df["Category"].unique(),
        default=df["Category"].unique(),
    )

    # Slider for filtering by salary
    min_salary = float(df["Salary"].min())
    max_salary = float(df["Salary"].max())
    salary_range = st.slider(
        "Select Salary Range ($):",  # Improved label
        min_value=min_salary,
        max_value=max_salary,
        value=(min_salary, max_salary),
    )

    # Filter the DataFrame
    filtered_df = df[df["Category"].isin(selected_categories)]
    filtered_df = filtered_df[
        (filtered_df["Salary"] >= salary_range[0]) & (filtered_df["Salary"] <= salary_range[1])
    ]

    st.dataframe(filtered_df)

    st.write(f"Number of results: {len(filtered_df)}") # Display number of results

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
