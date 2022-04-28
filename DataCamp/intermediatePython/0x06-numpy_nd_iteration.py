#!/usr/bin/env python3
""" numpy 2D iterate over all elements """
import numpy as np

np_height = np.array(['a', 'b', 'c', 'd', 'e'])
np_baseball = np.array([[1, 'x'], [2, 'y'], [3, 'z'], [8, 'aa']])

for x in np_height:
    print(x)

for x in np.nditer(np_baseball):
    print(x)
