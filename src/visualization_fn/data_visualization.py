import numpy as np
import pandas as pd
import plotly.express as px


def plot_index(df, index_name):
    """Plots the given index as a time series from
    the given dataframe. Makes the brackground transparent"""

    titles = {'EI': 'Education Index (EI)',
              'II': 'Income Index (II)',
              'LEI': 'Life Expectancy Index (LEI)'}
    fig = px.line(df, x="Year", y=index_name, color='Country', title=titles[index_name],
                  color_discrete_sequence=px.colors.qualitative.Dark2)
    fig.update_layout(title_x=0.5)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig
