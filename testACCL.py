#! /usr/bin/python
# -*- coding: utf-8 -*-

# This script makes Contour-Line graph.
# Y axis means ALPHA.
# X axis means BETA.
# This graph shows SIGMA/CN as color variation.

import csv
import sys
import os.path

import numpy as np
import matplotlib.pyplot as plt

# Extract parameter from CSV-filename.
def extractPARA(str, s1, s2):
  start = str.index(s1) + len(s1)
  end   = str.index(s2)

  buff=""
  for i in range(start, end, 1):
    buff += str[i]

  return buff


def makeCL(plt, tau_list, cn_list, un_list):
  X, Y = np.meshgrid(tau_list, un_list)
   
  plt.pcolormesh(X, Y, cn_list)

  plt.colorbar()

  plt.xlim(min(tau_list), max(tau_list))
  plt.ylim(min(un_list), max(un_list))

  plt.xlabel("tau")
  plt.ylabel("Unit number")

  plt.show()


argv = sys.argv

if (len(argv)<3):
  print "Too few data!!\n"
  quit()

fname = argv[1]
path = argv[2]

buff_fname = os.path.basename(fname)

tau_min = 0
tau_max = int(float(extractPARA(buff_fname, "_T", "_RASTER"))*0.95)

un_min = 0
un_max = int(extractPARA(buff_fname, "_U", "_T"))

un_list = np.arange(un_min, un_max+1)

# Read CSV file.
fuga      = np.loadtxt(fname, delimiter = ",")
hoge_hoge = fuga[:,1]
cn_list   = hoge_hoge.reshape(un_max+1, tau_max)

print fuga[2850,1]
print fuga[5700,1]
print cn_list
print cn_list[0,:]
print cn_list[1,:]
print cn_list[2,:]
print "len(cn_list)    * %d" % len(cn_list)
print "len(cn_list[0]) * %d" % len(cn_list[0])

tau_list = np.arange(tau_min, tau_max+1, 1)

i = 0
end = len(un_list)
makeCL(plt, tau_list[i:end], cn_list[:,i:end], un_list)


"""
i = 0
diff = len(un_list)
while i < len(tau_list):
  end = 0
  if (i >= len(tau_list)-diff):
    break
  else:
    end = i + diff

  suffix = buff_fname + "_" + str(i/diff+1) + "_SUB.png"

  i += diff


i   = len(tau_list)-diff
end = len(tau_list)

suffix = buff_fname + "_" + str(i/diff+1) + "_SUB.png"
makeCL(plt, tau_list[i:end], cn_list[i:end,:], un_list, path, suffix)
"""
