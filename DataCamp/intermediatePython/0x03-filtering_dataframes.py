#!/usr/bin/env python3
""" filter dataframes """
import pandas as pd
import numpy as np

brics = pd.read_csv("brics.csv", index_col=0)
print(brics, '\n')

# 1) select area
# filter huge countries, return a panda series
huge_area = brics["area"] > 8
print(huge_area, '\n')

# 2) apply the filter
print(brics[huge_area], '\n')

# also can use brics[brics["area"] > 8]

# Boolean operators
print(np.logical_and(brics["area"] > 8, brics["area"] < 10), '\n')

# apply to brics dataframe
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)], '\n')
