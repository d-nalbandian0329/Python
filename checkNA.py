#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg");

import csv

import os.path

import numpy as np
import matplotlib.pyplot as plt


def readFile(fname, sizeL, histL):
  buff = []
  with open(fname, "r") as f:
    reader = csv.reader(f)
    for data in reader:
      buff.append(data)

  idx  = 0
  last = len(buff)

  while idx < last:
    sizeL.append(int(buff[idx][0]))
    histL.append(int(buff[idx][1]))


def plotNA(fname, sizeL, histL):
  plt.xscale("log")
  plt.yscale("log")

  plt.plot(sizeL, histL, "bo")

  buff = os.path.basename(fname)
  name,ext = os.path.splitext(buff)
  plt.savefig("/Users/iwaitoshiya/Desktop/Graph_" + name + ".png")


if __name__ == "__main__":
  sizeL = []
  histL = []

  readFile("/Users/iwaitoshiya/Desktop/LAY100_CN3/RE_AVG_[LAY100_CN3_SIGMA0.500000].csv", sizeL, histL)

  plotNA(sizeL, histL)
