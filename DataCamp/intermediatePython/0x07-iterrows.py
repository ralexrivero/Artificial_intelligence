#!/usr/bin/env python3
""" iterate dictionary rows """
import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

for label, row in cars.iterrows():
    print(label)
    print(row, '\n')

for label, row in cars.iterrows():
    print("{}: {}".format(label, row['country']))

print()

for label, row in cars.iterrows():
    print("{}: {} => {} cpc".format(
          label, row['country'], row['cars_per_cap']))
