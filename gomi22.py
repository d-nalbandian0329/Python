#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import csv

import numpy as np

import matplotlib.pyplot as plt



if __name__ == "__main__":
  buff = []
  with open("/Users/iwaitoshiya/Desktop/cp_P0.300000D0.100000CN6TEST_STDP200.csv") as f:
    r = csv.reader(f)
    for data in r:
      buff.append(data)

  data_list = np.array(buff)

# header = next(reader) Skip reading.

  for data in data_list:
    print data



#  plt.savefig("/Users/iwaitoshiya/Desktop/testGP3.png")
