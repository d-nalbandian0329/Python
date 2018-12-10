#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import sys
import csv
import os.path

from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def makeAC_LG(plt, lst, i, path, suffix, xmajor, xminor, ymajor, yminor):
  fig, ax = plt.subplots()

  majorLocatorX = MultipleLocator(xmajor)
  majorFormatterX = FormatStrFormatter('%d')
  minorLocatorX = MultipleLocator(xminor)

  ax.xaxis.set_major_locator(majorLocatorX)
  ax.xaxis.set_major_formatter(majorFormatterX)

  # for the minor ticks, use no labels; default NullFormatter
  ax.xaxis.set_minor_locator(minorLocatorX)

  majorLocatorY = MultipleLocator(ymajor)
  majorFormatterY = FormatStrFormatter('%.3f')
  minorLocatorY = MultipleLocator(yminor)

  ax.yaxis.set_major_locator(majorLocatorY)
  ax.yaxis.set_major_formatter(majorFormatterY)

  # for the minor ticks, use no labels; default NullFormatter
  ax.yaxis.set_minor_locator(minorLocatorY)

  x_list = np.arange(i, i+len(lst), 1)

  label = "tau < max[%d] : %f     min[%d] : %f >"\
  %(lst.index(max(lst)), max(lst), lst.index(min(lst)), min(lst))

  plt.xlabel(label)
  plt.ylabel("Autocorrelation")

  plt.xlim(i, i+len(lst))
  plt.ylim(min(lst)-0.05, max(lst)+0.05)

  plt.title(suffix)

  plt.plot(x_list, lst, "r-")

  plt.savefig(path+suffix)
  plt.close()
  plt.clf()


argv = sys.argv

if (len(argv) < 3):
  print "Too few data!!\n"
  quit()

data_list = []
fname = argv[1]
path = argv[2]


y_list = []
with open(fname, "r") as f:
  reader = csv.reader(f)
  for data in reader:
    y_list.append(float(data[1]))

del y_list[0]

buff, hoge = os.path.splitext(os.path.basename(fname))

suffix = buff + "_ALL.png"
makeAC_LG(plt, y_list, 1, path, suffix, 500, 100, 0.1, 0.01)

i = 1
while i < len(y_list):
  if (i >= len(y_list)-100):
    lst = y_list[i:len(y_list)]
  else:
    lst = y_list[i:i+100]

  suffix = buff + "_" + str(i/100+1) + "_SUB.png"
  makeAC_LG(plt, lst, i, path, suffix, 100, 10, 0.1, 0.01)
  i += 100

