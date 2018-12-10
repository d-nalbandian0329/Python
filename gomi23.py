#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import csv

if __name__ == "__main__":
  data_list = []

  with open("/Users/iwaitoshiya/Desktop/P0.300000D0.100000CN6TEST_STDP200.csv", "r") as f:
    freader = csv.reader(f)
    for data in freader:
      data_list.append(data)

  ary = np.array(data_list)

  plt.subplots_adjust(left=0.02, right=1.00, top=1.00, bottom=0.03)

  for i in range(len(ary)):
    a = 0.8 - float(ary[i][4])
    if a >= 0.9:
      a = 0.9
    elif a <= 0.1:
      a = 0.1

    plt.plot([int(ary[i][1]),int(ary[i][3])], [int(ary[i][0]),int(ary[i][2])], "b-", alpha=a)

  plt.savefig("/Users/iwaitoshiya/Desktop/testCircuit.png")
