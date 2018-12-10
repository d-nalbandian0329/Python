#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
#matplotlib.use("Agg")

import matplotlib.font_manager
fontprop = matplotlib.font_manager.FontProperties(fname="/Library/Fonts/fonts-japanese-gothic.tff")

import numpy as np
import matplotlib.pyplot as plt

import csv

#
def rasterPlot(csv_list):
  xlist = []
  ylist = []

  i = 0
  while i < len(csv_list):
    xlist.append(float(csv_list[i][0]))
    ylist.append(float(csv_list[i][1]))
    i += 1

  return [xlist, ylist]


def splitGraph(list1, list2):
  plt.subplot()
  plt.plot()





if __name__ == "__main__":
  csv_list = []

  fname  = "/Users/iwaitoshiya/Desktop/u226136_NeuronalAvalanchesData"
  fname += "/CSV/Average/AVG_CN6[0.100000:5.001000]_sigma_f.csv"

  # File open and close automatically.
  # When break this loop, file-stream close.
  with open(fname, "r") as f:
    reader = csv.reader(f)
    for data in reader:
      csv_list.append(data)

  #start = float(csv_list[7][0])
  #end   = float(csv_list[][0])
  #diff  = float(csv_list[1][0]) - float(csv_list[0][0])

  #x = arange(start, end, diff)

  ret = rasterPlot(csv_list)

  start = 0.8;



  plt.plot(ret[0], ret[1], 'o')
  plt.show()


