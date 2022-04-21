#!/usr/bin/env python3
""" logical and, or and not in numpy array """

import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])


# generate boolean array
np_log_array = np.logical_and(my_house < 13, your_house < 15)
print(np_log_array)

print(np.logical_or(my_house < 13, your_house < 10))

print(np.logical_and(my_house < 10, your_house < 10))
