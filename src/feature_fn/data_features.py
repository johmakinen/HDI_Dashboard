import numpy as np
import pandas as pd


def add_indices(df):
    """Calculates the three indices that make up HDI"""
    res = df.copy()
    res['LEI'] = (res['Life_expectancy_at_birth']-20)/(85-20)
    res['EI'] = (res['Mean_years_of_schooling']/15 +
                 res['Expected_years_of_schooling']/18) / 2
    res['II'] = (np.log(res['Gross_national_income_per_capita']) -
                 np.log(100)) / (np.log(75000)-np.log(100))

    return res
