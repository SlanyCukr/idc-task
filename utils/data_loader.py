import pandas as pd
from numpy import ndarray


def load_adjust_data(data_filename: str, exchange_filename: str, local_country: str) -> pd.DataFrame:
    """
    Loads specified datasets and performs series of operations to create easy to use dataset.
    :param data_filename: Filename for the excel data dataset
    :param exchange_filename: Filename for the excel exchange dataset
    :param local_country: Country which we want to use
    :return: Easy to use dataset
    """
    # load datasets
    data_df = pd.read_excel(data_filename, 'Sheet0')
    exchange_df = pd.read_excel(exchange_filename, 'Sheet1')

    # annual revenue for each company in USD, rename
    data_df = data_df.groupby('Company').sum().reset_index()
    data_df.rename(columns={'Revenue': 'Revenue (USD)'}, inplace=True)

    # find needed data from exchange dataset; needed for finding annual revenue, finding local currency
    needed_data_from_exchange = exchange_df[exchange_df['Country'] == local_country]

    # annual revenue for each company in local currency
    data_df['Revenue (Local)'] = data_df['Revenue (USD)'] * needed_data_from_exchange['Annual Rate'].iloc[0]

    # calculate share
    total_revenue = data_df['Revenue (USD)'].sum()
    data_df['Share'] = (data_df['Revenue (USD)'] / total_revenue) * 100

    # total statistics - append new row to data dataframe
    data_df.loc[len(data_df.index)] = ['Total', total_revenue, data_df['Revenue (Local)'].sum(), data_df['Share'].sum()]

    # round to 2 decimal places
    data_df = data_df.round(2)

    # format value as strings - add currency or '%' and remove zero decimal point
    data_df['Revenue (USD)'] = '$' + data_df['Revenue (USD)'].astype(str)
    data_df['Revenue (USD)'] = data_df['Revenue (USD)'].str.replace(r'\.0', '', regex=True)

    # get local currency for `local_country`; it's plain string - like CZK, EUR, etc.
    local_currency = needed_data_from_exchange['Currency'].iloc[0]
    data_df['Revenue (Local)'] = f"{local_currency} " + data_df['Revenue (Local)'].astype(str)
    data_df['Revenue (Local)'] = data_df['Revenue (Local)'].str.replace(r'\.0', '', regex=True)

    data_df['Share'] = data_df['Share'].astype(str) + ' %'
    data_df['Share'] = data_df['Share'].str.replace(r'\.0', '', regex=True)

    return data_df


def select_local_countries(exchange_filename: str) -> ndarray:
    """
    Finds local countries in exchange dataset.
    :param exchange_filename: Filename of the dataset
    :return: Array of unique countries
    """
    exchange_df = pd.read_excel(exchange_filename, 'Sheet1')

    return exchange_df['Country'].values