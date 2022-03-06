
import numpy as np
import pandas as pd
from functools import reduce
import os


def process_raw_data():
    """A function to preprocess the raw data.
        We first read the csv files, then 
        we drop some unused information rows.
        Afterwards we find common countries for all dataset, 
        and combine them into a reuslting dataframe."""

    path_project = os.path.abspath(
        os.path.join(__file__, "../../.."))

    path_raw_data = path_project+'/data/raw/'
    path_processed_data = path_project+'/data/processed/'

    df_EYS = pd.read_csv(path_raw_data+'Expected years of schooling (years).csv',
                         skiprows=6, sep=',', encoding='latin-1')
    df_GNIpc = pd.read_csv(path_raw_data+'Gross national income (GNI) per capita (constant 2017 PPP$).csv',
                           skiprows=6, sep=',', encoding='latin-1')
    df_LE = pd.read_csv(path_raw_data+'Life expectancy at birth (years).csv',
                        skiprows=6, sep=',', encoding='latin-1')
    df_MYS = pd.read_csv(path_raw_data+'Mean years of schooling (years).csv',
                         skiprows=6, sep=',', encoding='latin-1')

    common_countries = set.intersection(set(df_EYS['Country']), set(
        df_GNIpc['Country']), set(df_LE['Country']), set(df_MYS['Country']))
    # n_countries = len(common_countries)

    keep_cols = np.r_[1:2, 2:df_EYS.shape[1]:2]
    df_EYS = df_EYS.iloc[:, keep_cols][df_EYS['Country'].isin(
        common_countries)].dropna(axis=0, subset=['Country'])
    df_GNIpc = df_GNIpc.iloc[:, keep_cols][df_GNIpc['Country'].isin(
        common_countries)].dropna(axis=0, subset=['Country'])
    df_LE = df_LE.iloc[:, keep_cols][df_LE['Country'].isin(
        common_countries)].dropna(axis=0, subset=['Country'])
    df_MYS = df_MYS.iloc[:, keep_cols][df_MYS['Country'].isin(
        common_countries)].dropna(axis=0, subset=['Country'])

    data_frames = [df_EYS.melt(id_vars='Country', var_name='Year', value_name='Expected_years_of_schooling'),
                   df_GNIpc.melt(id_vars='Country', var_name='Year',
                                 value_name='Gross_national_income_per_capita'),
                   df_LE.melt(id_vars='Country', var_name='Year',
                              value_name='Life_expectancy_at_birth'),
                   df_MYS.melt(id_vars='Country', var_name='Year',
                               value_name='Mean_years_of_schooling')
                   ]

    res = reduce(lambda left, right: pd.merge(left, right, on=['Country', 'Year'],
                                              how='inner'), data_frames)
    res.to_csv(path_processed_data+'processed_data.csv', index=False)

    return res


if __name__ == '__main__':

    df = process_raw_data()
    print(df.head())
