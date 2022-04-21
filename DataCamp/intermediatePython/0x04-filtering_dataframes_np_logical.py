#!/usr/bin/env python3
""" filtering dataframes using np logical_and logical_or """


import pandas as pd
import numpy as np

cars = pd.read_csv("cars.csv", index_col=0)
print(cars, '\n')

# medium: observation with cars_per_cap between 100 and 500

medium = np.logical_and(cars["cars_per_cap"] > 100, cars["cars_per_cap"] < 500)
print(cars[medium], '\n')


# other way
cpc = cars["cars_per_cap"]
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]
print(medium, '\n')
