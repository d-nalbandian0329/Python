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


def makeSPGraph(x_list, y_list, fname, prefix):
  xmajor = 0.5
  xminor = 0.1
  ymajor = 0.1
  yminor = 0.05

  fig, ax = plt.subplots()

  majorLocatorX = MultipleLocator(xmajor)
  majorFormatterX = FormatStrFormatter('%.1f')
  #minorLocatorX = MultipleLocator(xminor)

  ax.xaxis.set_major_locator(majorLocatorX)
  ax.xaxis.set_major_formatter(majorFormatterX)

  # for the minor ticks, use no labels; default NullFormatter
  #ax.xaxis.set_minor_locator(minorLocatorX)

  majorLocatorY = MultipleLocator(ymajor)
  majorFormatterY = FormatStrFormatter('%.1f')
  minorLocatorY = MultipleLocator(yminor)

  ax.yaxis.set_major_locator(majorLocatorY)
  ax.yaxis.set_major_formatter(majorFormatterY)

  # for the minor ticks, use no labels; default NullFormatter
  ax.yaxis.set_minor_locator(minorLocatorY)

  plt.xlabel("Sigma")
  plt.ylabel("Survival Probability")

  hoge, suffix = os.path.splitext(os.path.basename(fname))
  plt.title(hoge)

  title = hoge + ".png"

  plt.plot(x_list, y_list, "ro-")
  plt.savefig(prefix+title)

  plt.close()
  plt.clf()


argv = sys.argv

if(len(argv) < 3):
  print "Too few data!!"
  quit()

fname = argv[1]
stack_path = argv[2]

data = np.loadtxt(fname, delimiter=',')

'''
print data

print data[:,0]
print data[:,1]
'''

makeSPGraph(data[:,0], data[:,1], fname, stack_path)

