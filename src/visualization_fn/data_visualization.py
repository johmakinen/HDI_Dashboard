import numpy as np
import pandas as pd
import plotly.express as px


def plot_index(df, index_name):
    """Plots the given index as a time series from
    the given dataframe. Makes the brackground transparent"""

    titles = {'EI': 'Education Index (EI)',
              'II': 'Income Index (II)',
              'LEI': 'Life Expectancy Index (LEI)',
              'HDI': 'Human Development Index (HDI)'}
    fig = px.line(df, x="Year", y=index_name, color='Country', title=titles[index_name],
                  color_discrete_sequence=px.colors.qualitative.Dark2)
    fig.update_layout(title_x=0.5)
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
    })
    return fig


def plot_map(df, ind='HDI'):
    """This plots a map of the world.
        The colorscale shows the selected index."""

    titles = {'EI': 'Education Index (EI)',
              'II': 'Income Index (II)',
              'LEI': 'Life Expectancy Index (LEI)',
              'HDI': 'Human Development Index (HDI)'}
    fig = px.choropleth(df, locations="Country",  # used plotly express choropleth for animation plot
                        color=ind,
                        locationmode='country names',
                        # hover_name="Country",
                        hover_data=[ind],
                        title=titles[ind],
                        color_continuous_scale='rdylgn')
    fig.update_layout(
        autosize=True,
        # width=1200,
        # height=600,
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=25,
            pad=0
        ),
        title_x=0.48)
    return fig
