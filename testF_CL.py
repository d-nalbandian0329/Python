#! /usr/bin/python
# -*- coding: utf-8 -*-

# This script makes Contour-Line graph.
# Y axis means ALPHA.
# X axis means BETA.
# This graph shows SIGMA/CN as color variation.

import matplotlib
matplotlib.use("Agg")

import csv
import sys
import os.path

import math

import numpy as np
import matplotlib.pyplot as plt


argv = sys.argv

if (len(argv)<4):
  print "Too few data!!\n"
  quit()

fname = argv[1]
path = argv[2]
sub_title = argv[3]

alpha_min = 0.1
beta_min = 0.1

alpha_max = 5.0
beta_max = 5.0

diff = 0.1
dx = diff/2

alpha = np.arange(alpha_min, alpha_max+dx, diff)
beta  = np.arange(beta_min, beta_max+dx, diff)

alpha_len = len(alpha)
beta_len  = len(beta)


i = 0
data_list = np.zeros((beta_len, alpha_len))
with open(fname, "r") as f:
  reader = csv.reader(f)
  for data in reader:
    row = i / alpha_len
    col = i % alpha_len
    data_list[row][col] = math.log10(float(data[2]))
    i += 1

X, Y = np.meshgrid(beta, alpha)

plt.pcolormesh(X, Y, data_list)
plt.colorbar()

fuga = os.path.basename(fname)
hoge, suffix = os.path.splitext(fuga)

plt.title(sub_title+"\n"+hoge)

plt.xlabel("BETA")
plt.ylabel("ALPHA")

plt.savefig(path+hoge+".png")
