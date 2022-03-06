# Main code here
import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(layout="wide")


st.title('Human Development Index in the EU')

'This is a dashboard for visualizing Human Development Index (HDI), and the indices from which it is calculated.'
'HDI is calculated from various hand picked indices:'
'Below we have a cleaned dataset from the United Nations Development Programme'

DATA_PATH = 'data/processed/processed_data.csv'


@st.cache
def load_data():
    data = pd.read_csv(DATA_PATH)
    return data


# data_load_state = st.text('Loading data...')
data = load_data()
# data_load_state.text("Done!")

st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)
