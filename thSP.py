#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import sys
import os.path

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

argv = sys.argv


def makeSPGraph(x_list, y_list, path):
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

  plt.ylim(0.0, 1.0)

  plt.plot(x_list, y_list, "bo-")
  plt.savefig(path)

  plt.close()
  plt.clf()


if(len(argv) < 3):
  print "Too few data!!"
  quit()

fname      = argv[1]
stack_path = argv[2]

# Load file.
data = np.loadtxt(fname, delimiter=",")

# Get Filename from Filepath.
hoge = os.path.basename(fname)
# Separate filename to name and suffix.
fuga, suffix = os.path.splitext(hoge)

path = stack_path + fuga + ".png"

makeSPGraph(data[:,0], data[:,1], path)

