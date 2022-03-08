# Main code here
import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

# My modules
from src.feature_fn.data_features import add_indices
from src.visualization_fn.data_visualization import plot_index


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
    return data.query('Year >= 2010')


@st.experimental_memo
def select_data(df, countries: list[str]):
    return df.query('Country in @countries')


@st.experimental_memo
def add_ind(df):
    return add_indices(df)


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
    st.title('Human Development Index (HDI)')

with t2:
    st.write("")
    st.write("")
    st.write("""
    **By Johannes Mäkinen** | [johmakinen.github.io](https://johmakinen.github.io)
    """)

st.write("")

st.markdown("""_\"The HDI was created to emphasize that people and their capabilities should be the ultimate criteria for assessing the development of a country,
 not economic growth alone. The HDI can also be used to question national policy choices, asking how two countries with
  the same level of GNI per capita can end up with different human development outcomes.\"_ - United Nations Development Program""")
st.markdown("""In short, HDI measures the development level of a country or area by combining common metrics.
            Though the measure has gotten critisism for not accounting racism, inequality and history of colonial actions,
            the metric itself is quite interesting to study. There are also other metrics that calculate the HDI by accounting for
            the aforementioned problems.""")


st.header("HDI mathematically")


with st.container():
    image = Image.open(cwd+'\\figures\\draw_hdi_form.png')
    st.image(image,
             caption="HDI calculated from its component indices.",
             output_format='PNG')

st.markdown("""We can see that HDI is calculated using three main components: Health, Education and the standard of living.
                The values are scaled using the min-max method to make them comparable between countries. According to UN,
                the transformation function from income to capability is likely to be concave, and thus a logarithm is
                used when calculating the Income Index.
            """)

df_static_norm = pd.DataFrame([['Health', 'Education', 'Education', 'Standard of living'],
                               ['Life expectancy', 'Expected years of schooling',
                                   'Mean years of schooling', 'GNI per capita ($)'],
                               [20, 0, 0, 100],
                               [85, 18, 15, 75000]],
                              index=['Dimension', 'Indicator', 'Minimum', 'Maximum']).T.astype(str)

st.write(df_static_norm)

st.header("HDI numbers presented")

st.write("""Below we have a cleaned dataset from the United Nations Development Programme.
 For all the following tables and charts, you can select the countries from the sidebar on the left. 
 The Gross National Income is in dollars ($).""")

st.write(current_data.style.format({'Expected_years_of_schooling': "{:.2f}",
                                    'Mean_years_of_schooling': "{:.2f}",
                                    'Life_expectancy_at_birth': "{:.2f}",
                                    'Gross_national_income_per_capita': "{:.0f}"}))
data_ind = add_ind(current_data)

p1, _, p2 = st.columns((3, 0.2, 3))
with p1:
    st.plotly_chart(plot_index(data_ind, 'LEI'), use_container_width=True)

with p2:
    st.plotly_chart(plot_index(data_ind, 'EI'), use_container_width=True)
