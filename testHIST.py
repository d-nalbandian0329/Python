#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import matplotlib.mlab as mlab

import csv

if __name__ == "__main__":
  data_list = []

  for i in range(50, 201, 50):
    fname = "/Users/iwaitoshiya/Desktop/STDP_TEST/"
    buff  = "LN" + str(i) + "BIN0.020P0.300D0.100CN6HIST200"

    fname += (buff + ".csv")
    with open(fname, "r") as f:
      reader = csv.reader(f)
      for data in reader:
        data_list.append(data)

    ary = np.array(data_list)

    n,bins,patches = plt.hist(ary, bins = 10, range = (0.0, 1.0))
    plt.plot(bins, "r--", linewidth = 1)

    path = "/Users/iwaitoshiya/Desktop/Histogram/"
    path += (buff + ".png")
    plt.savefig(path)
