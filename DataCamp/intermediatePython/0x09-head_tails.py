#!/usr/bin/env python3
""" head or tails . Generate a random walk based on previous random number """
import numpy as np

np.random.seed(123)
np.random.randint(0, 2)

outcomes = []

for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")

print(outcomes)
