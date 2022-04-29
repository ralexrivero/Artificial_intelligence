#!/usr/bin/env python3
""" apply() to add a new column in a eficient mode """
import pandas as pd


cars = pd.read_csv('cars.csv', index_col=0)

cars['COUNTRY'] = cars['country'].apply(str.upper)
print(cars)
