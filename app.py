import streamlit as st
import pandas as pd

st.title("Streamlit App")

try:
    df = pd.read_csv("data.csv")

    # Multiselect widget for filtering by category
    selected_categories = st.multiselect(
        "Select Categories:", options=df["Category"].unique(), default=df["Category"].unique()
    )

    # Slider for filtering by salary
    min_salary = float(df["Salary"].min())
    max_salary = float(df["Salary"].max())
    salary_range = st.slider(
        "Select Salary Range:", min_value=min_salary, max_value=max_salary, value=(min_salary, max_salary)
    )

    # Filter the DataFrame
    filtered_df = df[df["Category"].isin(selected_categories)]
    filtered_df = filtered_df[
        (filtered_df["Salary"] >= salary_range[0]) & (filtered_df["Salary"] <= salary_range[1])
    ]

    st.dataframe(filtered_df)

except FileNotFoundError:
    st.error("Error: data.csv not found.")
except KeyError as e:
    st.error(f"Error: Column '{e}' not found in data.csv.  Make sure 'Salary' and 'Category' columns exist.")
except ValueError:
    st.error("Error: 'Salary' column contains non-numeric values. Please ensure it only contains numbers.")
