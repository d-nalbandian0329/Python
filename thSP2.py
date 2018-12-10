#!/usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import sys
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

def setInit():
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



argv = sys.argv

if(len(argv) < 3):
  print "Too few data!!"
  quit()

num = len(argv)
flist = [(x, extractPARA(x, "CN", ".csv")) for x in argv[1:num-1]]
stack_path = argv[num-1]

var_line = ["ro-", "gx-", "b^-", "cd-", "mp-", "yv-"]

setInit()

hoge = ("SP_CNchange_%s_%s[theory].png" % (flist[0][1], flist[len(flist)-1][1]))
path = stack_path + hoge

vn = len(var_line)
idx = 0
for fset in flist:
  # Load file.
  data = np.loadtxt(fset[0], delimiter=",")
  plt.plot(data[:,0], data[:,1], var_line[idx%vn], label = ("C=%s" % fset[1]))
  idx += 1

plt.legend(loc="lower right")

plt.savefig(path)

