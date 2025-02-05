import streamlit as st
import pandas as pd
import plotly.express as px

def get_fact(dataframe):
    return dataframe["Fact"].values[0]

def get_image(dataframe):
    return dataframe["Image"].values[0]

# SOLUTION
@st.cache_data
def load_data():
    return pd.read_csv("data/animal_counts.csv").sort_values(["Common_name", "Year"])

animal_df = load_data()
animals = animal_df["Common_name"].unique()

st.title("Animal Numbers Over Time")

selected_animal = st.selectbox("Select an Animal", animals)

button_run_pressed = st.button("Run")

if button_run_pressed:

    # Filtering
    single_animal_df = animal_df[animal_df["Common_name"] == selected_animal]

    # Setting up tabs
    tab1, tab2 = st.tabs(["Animal Details", "Numbers over time"])

    # Displaying the overall data for the animal in tab 1
    with tab1:

        st.subheader(selected_animal)

        col1, col2 = st.columns(2)

        with col1:
            st.write(get_fact(single_animal_df))

        with col2:
            st.image(get_image(single_animal_df))

    # Displaying the yearly dataframe and table in the final output
    with tab2:
        st.plotly_chart(
                px.line(single_animal_df,
                            x="Year",
                            y="Count")
            )

        st.dataframe(single_animal_df[["Year", "Count"]], hide_index=True)
