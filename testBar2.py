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


data_list = []
fname = "/Users/iwaitoshiya/Desktop/TEST_HIST/LN100PMAX3.50000PMIN0.50000CN10.csv"
path = "/Users/iwaitoshiya/Desktop/test.png"

x_list = []
y_list = []
with open(fname, "r") as f:
  reader = csv.reader(f)
  for data in reader:
    x_list.append(float(data[0]))
    y_list.append(float(data[1]))

plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)

plt.title("Test")

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


plt.xlabel("Fire-probability")
plt.ylabel("Unit-Count Ratio")

plt.bar(x_list, y_list, width=0.02)

plt.savefig(path)
