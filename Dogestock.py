#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  5 11:24:54 2021

@author: kyledluge
"""

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2020, 12, 31)

df = web.DataReader('Doge-USD', 'yahoo', start, end)
print(df.head())
print("")
print(df.tail())


