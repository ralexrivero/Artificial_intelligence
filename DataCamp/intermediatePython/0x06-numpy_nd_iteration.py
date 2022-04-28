#!/usr/bin/env python3
""" numpy 2D iterate over all elements """
import numpy as np

np_height = np.array([1, 2, 3, 4, 5])
np_baseball = np.array([[1, 3], [2, 4], [3, 6], [8, 9]])

for x in np_height:
    print(x)

for x in np.nditer(np_baseball):
    print(x)
