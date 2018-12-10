#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path

import csv
import numpy as np
import matplotlib.pyplot as plt

"""
argv = sys.argv
if (len(argv) < 3):
  print "Too few data!!"
  quit()
"""

fname = "/Users/iwaitoshiya/Desktop/DATA_CN20PMAX0.9980PMIN0.0001SIGMA1.000/LN50/ALPHA0.500/"
fname += "LN50DX0.100ALPHA0.500BETA0.500CN20SIGMA1.000.csv"

list = []
with open(fname, "r") as f:
  data_list = csv.reader(f)
  for data in data_list:
    list.append(data)

array = np.array(list)

sigma = 1.0
cn = 20
diff = 0.02

buff = ""
target = int(sigma/cn/diff)*diff
for i in range(len(array)):
  if (target==float(array[i][0])):
    buff = array[i][1]
    break
print array
print "buff : " + buff
