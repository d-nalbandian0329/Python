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


# Extract parameter from CSV-filename.
def extractPARA(str, s1, s2):
  start = str.index(s1) + len(s1)
  end   = str.index(s2)

  buff=""
  for i in range(start, end, 1):
    buff += str[i]

  return buff


def makeHIST(fname, path, y_list):
  base = os.path.basename(fname)
  unit = int(extractPARA(base, "_U", "_T"))
  step = int(extractPARA(base, "_T", "_RASTER"))

  x_major = (int)(unit/5)
  x_minor = (int)(unit/10)
  y_max   = 500
  y_major = 100
  y_minor = 10


  x_list = np.arange(1, unit+1, unit/100)

  fig, ax = plt.subplots()

  majorLocatorX = MultipleLocator(x_major)
  majorFormatterX = FormatStrFormatter('%d')
  minorLocatorX = MultipleLocator(x_minor)

  ax.xaxis.set_major_locator(majorLocatorX)
  ax.xaxis.set_major_formatter(majorFormatterX)

  # for the minor ticks, use no labels; default NullFormatter
  ax.xaxis.set_minor_locator(minorLocatorX)
 
  majorLocatorY = MultipleLocator(y_major)
  majorFormatterY = FormatStrFormatter('%d')
  minorLocatorY = MultipleLocator(y_minor)

  ax.yaxis.set_major_locator(majorLocatorY)
  ax.yaxis.set_major_formatter(majorFormatterY)
  
  # for the minor ticks, use no labels; default NullFormatter
  ax.yaxis.set_minor_locator(minorLocatorY)

  buff, hoge = os.path.splitext(base)
  
  path += (buff+".png")
  
  plt.title(buff)
  
  plt.xlabel("Fire count")
  plt.ylabel("Step count")
  
  
  plt.xlim(1, unit)
  plt.ylim(0, 500)
  
  plt.bar(x_list, y_list, width=unit/100, color='g')
  
  plt.savefig(path)


argv = sys.argv

if (len(argv) < 3):
  print "Too few data!!\n"
  quit()

data_list = []
fname = argv[1]
path  = argv[2]

y_list = []
with open(fname, "r") as f:
  reader = csv.reader(f)
  for data in reader:
    y_list.append(int(data[1]))

makeHIST(fname, path, y_list)

