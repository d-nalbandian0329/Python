#! /usr/bin/python
# -*- coding: utf-8 -*-

# This script makes Line Graph.

"""
import matplotlib
matplotlib.use("Agg")
"""

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


argv = sys.argv

if (len(argv) < 3):
  print "Too few data!!\n"
  quit()

fname = argv[1]
path = argv[2]

hoge = os.path.basename(fname)

ln = int(extractPARA(hoge, "LN", "DX"))

data_array = np.zeros((ln, 3))
xlist = range(1, (ln+1), 1)

with open(fname, "r") as f:
  reader = csv.reader(f)
  i = 0
  for data in reader:
    data_array[i][0] = int(data[0])
    data_array[i][1] = int(data[1])
    data_array[i][2] = int(data[2])
    i += 1

plt.plot(xlist, data_array[:,0], "r-o")
plt.plot(xlist, data_array[:,1], "g-o")
plt.plot(xlist, data_array[:,2], "b-o")
"""
buff, hoge = os.path.splitext(os.path.basename(fname))

path += (buff+".png")

plt.title(buff)
"""

plt.xlabel("Learning count")
plt.ylabel("Fired-unit count\nFinal reached layer")

plt.xlim(1, ln)

plt.show()

"""
plt.savefig(path)
"""
