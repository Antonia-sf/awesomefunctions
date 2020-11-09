# -*- coding: UTF-8 -*-

# Import from standard library
import os
import awesomefunctions
import pandas as pd
# Import from our lib
from awesomefunctions.lib import clean_data
from awesomefunctions.lib import data_cleaning
import pytest

def test_data_cleaning():
    assert data_cleaning('My name is 333') == 'my name is '

def test_clean_data():
    datapath = os.path.dirname(os.path.abspath(awesomefunctions.__file__)) + '/data'
    df = pd.read_csv('{}/data.csv.gz'.format(datapath))
    first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
    assert list(df.columns)[:6] == first_cols
    assert df.shape == (999, 142)
    out = clean_data(df)
    assert out.shape == (985, 119)
