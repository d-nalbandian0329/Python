#!/usr/bin/python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

array = np.loadtxt("/Users/iwaitoshiya/Desktop/LN100DX0.100ALPHA0.500BETA5.000CN30SIGMA1.000.csv", delimiter=",")
array2 = np.zeros((5, 5, 5))

print array[0]
print array[0][0]

print array[:,0]
print array[:,1]

print array[0:2,1]

array2[:,1:4:2,2] = 1
print array2
print array2[:,1:4:2,2]
