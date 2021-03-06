import numpy as np
import pytest
from src.data_fn.data_processing import process_raw_data
from src.feature_fn.data_features import add_indices


def test_process_raw_data():
    """Test that the processing is done correctly.
        Mainly,
        1. Resulting data is not empty
        2. No inf values (Nan, negative and large are allowed)
        3. Most of the data is not Nan
        """
    test_data = process_raw_data()
    # Not empty
    assert test_data.empty == False
    # No inf values
    assert test_data.isin([np.inf, -np.inf]).sum().sum() == 0
    # 'There is not colun for which there are over 15% nan values'
    assert test_data.isnull().mean().max() < 15/100
    # 'There is no country for which there are only a few years of data'
    assert test_data.T.isnull().mean().max() < 80/100


def test_indexed_data():
    test_data = add_indices(process_raw_data())
    # Not empty
    assert test_data.empty == False
    # No inf values
    assert test_data.isin([np.inf, -np.inf]).sum().sum() == 0
    # 'There is not colun for which there are over 15% nan values'
    assert test_data.isnull().mean().max() < 15/100
    # 'There is no country for which there are only a few years of data'
    assert test_data.T.isnull().mean().max() < 85/100


# Instructions:
# Run testsuite from the main directory 'HDI_Dashboard'.
# python -m pytest -r unitTest\test_data_processing.py #from main dir
