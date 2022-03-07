# Main code here
import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image


st.set_page_config(
    page_title="Human Development Index",
    layout='wide',
    initial_sidebar_state='auto',
)


# ----------------------------------------------------------------------------------------
# FUNCTIONS

cwd = os.getcwd()
DATA_PATH = cwd+'\data\processed\processed_data.csv'


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
st.sidebar.title("Select countries/areas to be presented")
selected_countries = st.sidebar.multiselect(
    '', set(data['Country'].values), default=['World'])
current_data = select_data(data, countries=selected_countries)


# ----------------------------------------------------------------------------------------
# LAYOUT
t1, t2 = st.columns(2)
with t1:
    st.title('Human Development Index')

with t2:
    st.write("")
    st.write("")
    st.write("""
    **By Johannes Mäkinen** | [johmakinen.github.io](https://johmakinen.github.io) 
    """)

st.write("")
st.markdown("""This is a dashboard for visualizing Human Development Index (HDI),
    and the indices from which it is calculated.""")


st.header("So how is the HDI explicitly calculated?")

with st.container():
    image = Image.open(cwd+'\\figures\\hdi_2020.jpg')
    st.image(image,
             caption="HDI calculated from its component indices. Source: en.wikipedia.org/wiki/Human_Development_Index")

st.markdown("""We can see that HDI is calculated using three main components. These components can be further inspected.""")
col1, col2 = st.columns(2)

with col1:
    image = Image.open(cwd+"\\figures\\hdi_new_method.png")
    st.image(image, caption='Source en.wikipedia.org/wiki/Human_Development_Index')

with col2:
    image = Image.open(cwd+"\\figures\\hdi_old_method.jpg")
    st.image(image, caption='Source: en.wikipedia.org/wiki/Human_Development_Index')

st.subheader("Now that we know what the HDI stands for and how its calculated, we can visualize the data that we have on different countries.")


st.write("Below we have a cleaned dataset from the United Nations Development Programme")

st.write(current_data)
