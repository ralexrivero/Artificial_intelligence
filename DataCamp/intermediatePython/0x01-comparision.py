#!/usr/bin/env python3
""" boolean comparison """
import numpy as np

# classic comparision in python objects

print(2 == (1 + 1))
print("intermediate" != "beginner")
print(True != False)
print("Python" != "python")
print(1 == True)

""" numpy comparison """


my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

"""
evaluate element wise if my_house is greater than or equal to 18
return list of booleans
"""
print(my_house >= 18)

print(my_house < your_house)
