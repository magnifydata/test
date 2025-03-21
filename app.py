import streamlit as st
import pandas as pd
import plotly.express as px

# Set a wider default layout
st.set_page_config(layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .reportview-container .main .block-container{
        max-width: 1200px;
    }
    h1 {
        color: #2E86C1 !important; /* Steel Blue */
    }
    h2 {
        color: #1A5276 !important; /* Dark Blue */
    }
    .stDataFrame {
        border: 1px solid #EBF4FA;
        border-radius: 5px;
        padding: 10px;
        background-color: #F0F8FF; /* AliceBlue */
    }
    .streamlit-expanderHeader {
        font-size: 1.2em !important;
        font-weight: bold !important;
    }
    [data-testid="stSidebar"] {
        background-color: #D4E6F1; /* Light Blue */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Use Markdown/HTML to style the title
st.markdown("<h1 style='color: green;'>Employee Data Filter</h1>", unsafe_allow_html=True)

try:
    df = pd.read_csv("data.csv")

    # Calculate summary metrics
    total_employees = len(df)
    average_salary = df["Salary"].mean()

    with st.sidebar:  # Put sidebar elements in a 'with' block
        st.header("Filter Options")

        # Multiselect widget for filtering by category (in the sidebar)
        selected_categories = st.multiselect(
            "Select Employee Categories:",
            options=df["Category"].unique(),
            default=df["Category"].unique(),
        )

        # Multiselect widget for filtering by department
        selected_departments = st.multiselect(
            "Select Departments:",
            options=df["Department"].unique(),
            default=df["Department"].unique(),
        )

        # Slider for filtering by salary (in the sidebar)
        min_salary = float(df["Salary"].min())
        max_salary = float(df["Salary"].max())
        salary_range = st.slider(
            "Select Salary Range ($):",
            min_value=min_salary,
            max_value=max_salary,
            value=(min_salary, max_salary),
        )

    # Filter the DataFrame
    filtered_df = df[df["Category"].isin(selected_categories)]
    filtered_df = filtered_df[df["Department"].isin(selected_departments)] # Added department filter
    filtered_df = filtered_df[
        (filtered_df["Salary"] >= salary_range[0]) & (filtered_df["Salary"] <= salary_range[1])
    ]

    # Display metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Employees", total_employees)
    with col2:
        st.metric("Average Salary", f"${average_salary:,.2f}")  # Format with commas and 2 decimals

    # Calculate average salary per category for the filtered data
    avg_salary_per_category = filtered_df.groupby("Category")["Salary"].mean().reset_index()

    # Create two columns for layout (adjust the ratio)
    col1, col2 = st.columns([3, 2])  # DataFrame takes 3/5, graph takes 2/5

    with col1:
        with st.expander("Employee Information", expanded=False):  # Add expander
            st.markdown("<h2 style='text-align: left;'>Employee Information</h2>", unsafe_allow_html=True)
            st.dataframe(filtered_df)
            st.write(f"Number of results: {len(filtered_df)}")

    with col2:
        # Chart type selector
        chart_type = st.selectbox("Select Chart Type:", ["Bar Chart", "Pie Chart", "Scatter Chart"])

        if chart_type == "Bar Chart":
            fig = px.bar(
                avg_salary_per_category,
                x="Category",
                y="Salary",
                labels={"Category": "Employee Category", "Salary": "Average Salary ($)"},
                title="Average Salary per Employee Category",
                height=400  # Adjust height as needed
            )
        elif chart_type == "Pie Chart":
            fig = px.pie(
                avg_salary_per_category,
                values="Salary",
                names="Category",
                title="Average Salary per Employee Category",
                height=400  # Adjust height as needed
            )
        elif chart_type == "Scatter Chart":
            # Add Age to scatter chart
            fig = px.scatter(
               filtered_df, # scatter charts takes the entire data frame.
               x="Category",
               y="Salary",
               size="Age",
               color="Category",
               hover_data=['Name', 'Age', 'City'],
               labels={"Category": "Employee Category", "Salary": "Salary ($)"},
               title="Salary vs Category (Size: Age)",
               height=400 # Adjust height as needed
           )

        st.caption(" ")  # Add a small caption for spacing
        st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("Error: data.csv not found.")
except KeyError as e:
    st.error(
        f"Error: Column '{e}' not found in data.csv.  Make sure 'Salary' and 'Category' and 'Department' columns exist."
    )
except ValueError:
    st.error(
        "Error: 'Salary' column contains non-numeric values. Please ensure it only contains numbers."
    )
