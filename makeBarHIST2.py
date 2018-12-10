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

x_list = np.arange(0.0, 1.0, 0.02)


fig, ax = plt.subplots()

majorLocatorX = MultipleLocator(0.1)
majorFormatterX = FormatStrFormatter('%.1f')
minorLocatorX = MultipleLocator(0.02)

ax.xaxis.set_major_locator(majorLocatorX)
ax.xaxis.set_major_formatter(majorFormatterX)

# for the minor ticks, use no labels; default NullFormatter
ax.xaxis.set_minor_locator(minorLocatorX)

majorLocatorY = MultipleLocator(0.1)
majorFormatterY = FormatStrFormatter('%.1f')
minorLocatorY = MultipleLocator(0.05)

ax.yaxis.set_major_locator(majorLocatorY)
ax.yaxis.set_major_formatter(majorFormatterY)

# for the minor ticks, use no labels; default NullFormatter
ax.yaxis.set_minor_locator(minorLocatorY)



buff, hoge = os.path.splitext(os.path.basename(fname))

path += (buff+".png")

plt.title(buff)

plt.xlabel("Fire-probability")
plt.ylabel("Unit-Count Ratio")


plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)

plt.bar(x_list, y_list, width=0.02)

plt.savefig(path)
