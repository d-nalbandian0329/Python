#! /usr/bin/python
# -*- coding=UTF-8 -*-

#import matplotlib
#matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import csv
import sys
import os.path

from matplotlib.ticker import MultipleLocator, FormatStrFormatter


def setTicks():
  xmajor = 0.5
  ymajor = 0.1
  yminor = 0.05

  fig, ax = plt.subplots()

  plt.grid(True)

  majorLocatorX = MultipleLocator(xmajor)
  majorFormatterX = FormatStrFormatter('%.1f')

  ax.xaxis.set_major_locator(majorLocatorX)
  ax.xaxis.set_major_formatter(majorFormatterX)

  majorLocatorY = MultipleLocator(ymajor)
  majorFormatterY = FormatStrFormatter('%.1f')
  minorLocatorY = MultipleLocator(yminor)

  ax.yaxis.set_major_locator(majorLocatorY)
  ax.yaxis.set_major_formatter(majorFormatterY)

  # for the minor ticks, use no labels; default NullFormatter
  ax.yaxis.set_minor_locator(minorLocatorY)

  plt.xlabel("Sigma", fontsize=20)
  plt.ylabel("Survival Probability", fontsize=20)

  plt.xticks(fontsize=20)
  plt.yticks(fontsize=20)

argv = sys.argv

if(len(argv) < 5):
  print "Too few data!!"
  quit()

fname1 = argv[1]
fname2 = argv[2]
fname3 = argv[3]
fname4 = argv[4]


setTicks()

data = np.loadtxt(fname1, delimiter=',')
plt.plot(data[:,0], data[:,1], "ro-", label="C=110")

data = np.loadtxt(fname2, delimiter=',')
plt.plot(data[:,0], data[:,1], "gx-", label="C=130")

data = np.loadtxt(fname3, delimiter=',')
plt.plot(data[:,0], data[:,1], "b^-", label="C=150")

data = np.loadtxt(fname4, delimiter=',')
plt.plot(data[:,0], data[:,1], "cd-", label="C=170")

data = np.loadtxt(fname4, delimiter=',')
plt.plot(data[:,0], data[:,1], "mp-", label="C=190")

plt.legend(loc="lower right")

title="/Users/iwaitoshiya/Desktop/SP_CN110_190[theory].png"
plt.savefig(title)

