# Main code here
import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(
    page_title="Human Development Index",
    layout='wide',
    initial_sidebar_state='auto',
)

# FUNCTIONS
DATA_PATH = 'data/processed/processed_data.csv'


@st.experimental_memo
def load_data():
    data = pd.read_csv(DATA_PATH)
    return data


@st.experimental_memo
def select_data(df, countries: list[str]):
    return df.query('Country in @countries')


# Get full dataset and cache it (6k rows, should be doable)
data = load_data()

# Select data according to the input
selected_countries = st.sidebar.multiselect(
    '', set(data['Country'].values), default=['World'])
current_data = select_data(data, countries=selected_countries)


# LAYOUT
t1, t2 = st.columns(2)
with t1:
    st.title('Human Development Index in the EU')

with t2:
    st.write("")
    st.write("")
    st.write("""
    **By Johannes Mäkinen** | [johmakinen.github.io](https://johmakinen.github.io) 
    """)

st.write("")
st.markdown("""This is a dashboard for visualizing Human Development Index (HDI),
 and the indices from which it is calculated. HDI is calculated from various hand picked indices:""")

# Equations here

st.write("Below we have a cleaned dataset from the United Nations Development Programme")

st.write(current_data)
