#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

import sys
import csv
import os.path


argv = sys.argv

if (len(argv) < 3):
  print "Invalid argument.\n"
  quit()

data_list = []

fname = argv[1]
# Data stock place.
path  = argv[2]

with open(fname, "r") as f:
  reader = csv.reader(f)
  for data in reader:
    data_list.append(data)

ary = np.array(data_list)

n, bins, patches = plt.hist(ary, bins=20, range=(0.0, 1.0), normed=True)
line = mlab.normpdf( bins, 0, 1)
plt.plot(bins, line, 'r--', linewidth=1)

buff, hoge = os.path.splitext(os.path.basename(fname))

path += (buff + ".png")

plt.title(buff)
plt.xlabel("Fire-probability")
plt.ylabel("Unit Count [ x${10^4}$ ]")

plt.savefig(path)
