# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:29:04 2024

@author: TUSHAR SINGH
"""
import pandas as pd
import matplotlib.pyplot as plt

filename='2012-2013 Solar home electricity data v2.csv'
d_raw = pd.read_csv(filename,skiprows=1,parse_dates=['date'], dayfirst=True,na_filter=False, dtype={'Row Quality': str})


result_df = d_raw.groupby(['Customer', 'Consumption Category']).mean().reset_index()
result_df.to_csv('mean_data.csv', index=False)