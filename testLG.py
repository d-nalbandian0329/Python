#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib.pyplot as plt

import sys
import csv
import os.path


data_array = np.zeros((10, 3))
i = 0
for n in range(1, 11):
  data_array[i][0] = n
  data_array[i][1] = n * 2
  data_array[i][2] = n * 3
  i += 1

print data_array[:,0]
print data_array[:,1]
print data_array[:,2]

print data_array

"""
plt.xlim(0, 10)
plt.ylim(0, 10)

plt.xlabel("Learning count")
plt.ylabel("Fired-unit count\nFinal reached layer")

plt.plot(xlist, ylist, "r-o")

plt.show()
"""
