#! /usr/bin/python
# -*- coding: utf-8 -*-

import csv

import numpy as np
import matplotlib.pyplot as plt

alpha = np.arange(0.5, 5.05, 0.1)
beta  = np.arange(0.5, 5.05, 0.1)

a = np.random.rand(46, 46)

print alpha[45]
print beta[45]

fname = "/Users/iwaitoshiya/Desktop/testData.csv"
i = 0
with open(fname, "w") as f:
  while i < len(alpha):
    j = 0
    while j < len(beta):
      f.write("%f,%f,%f\n" % (alpha[i], beta[j], a[i][j]))
      j += 1
    i += 1
