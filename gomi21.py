#! /usr/bin/python
# -*- coding: utf-8 -*-

import csv

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

# default properties
NUM = 200
LAY = 200
CN  = 6

dest     = []
strength = [[]]

def readCSV(fname):
  data_list = []
  with open(fname, "r") as f:
    # Read CSV file for each line.
    reader = csv.reader(f)
    for data in reader:
      data_list.append(data)

  NUM = int(data_list[0][0])
  LAY = int(data_list[1][0])
  CN  = int(data_list[2][0])

  idx = 3
  for j in range(LAY):
    for i in range(NUM):
      for k in range(CN):
        dest.append([int(data_list[idx][2]),int(data_list[idx][3])])
        strength.append(float(data_list[idx][4]))
        idx += 1


def init():
  xlist = []
  ylist = []

  i = 0
  while i < NUM:
    xlist.append(i)
    i += 1

  i = 0
  while i < LAY:
    ylist.append(i)
    i += 1

  for j in range(len(xlist)):
    for i in range(len(ylist)):
      plt.plot(xlist[i], ylist[j], "ro")


def test_plot():
  idx = 0
  num = 0
  lay = 0

  while idx < len(dest):
    i = idx / CN

    plt.plot([lay,dest[idx][1]], [num,dest[idx][0]])

    num += 1
    if num >= NUM:
      lay += 1
      num = 0


if __name__ == "__main__":
  init()

  fname = "/Users/iwaitoshiya/Desktop/cp_P0.300000D0.100000CN6TEST_STDP200.csv"
  readCSV(fname)

  test_plot()

  plt.savefig("/Users/iwaitoshiya/Desktop/test_circuit1.png")

  plt.show()
