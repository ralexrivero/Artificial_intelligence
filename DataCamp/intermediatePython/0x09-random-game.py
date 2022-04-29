#!/usr/bin/env python3
""" generate random using fixed seed """
import numpy as np

np.random.seed(123)
print(np.random.randint(1, 7))
