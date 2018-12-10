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


def makeCL(plt, tau_list, cn_list, un_list, path, suffix):
  X, Y = np.meshgrid(tau_list, un_list)
   
  #plt.pcolormesh(X, Y, cn_list)
  fig,ax = plt.subplots()
  val = np.linspace(0.0, 1.0, 20, endpoint = True)
  nn = plt.contourf(X, Y, cn_list, val)
  plt.colorbar(nn, ticks = val)

  plt.title(suffix)

  plt.xlim(min(tau_list), max(tau_list))
  plt.ylim(min(un_list), max(un_list))

  plt.xlabel("tau")
  plt.ylabel("Unit number")

  #plt.figure(figsize=(20,20))

  plt.savefig(path+suffix)
  # Close file stream.
  plt.close()
  # Clear graph in buffer.
  plt.clf()


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

tau_list = np.arange(tau_min, tau_max, 1)

i = 0
diff = len(un_list)
while i < len(tau_list):
  end = 0
  if (i >= len(tau_list)-diff):
    break
  else:
    end = i + diff

  suffix = buff_fname + "_" + str(i/diff+1) + "_SUB.png"
  makeCL(plt, tau_list[i:end], cn_list[:,i:end], un_list, path, suffix)

  i += diff


i   = len(tau_list)-diff
end = len(tau_list)

suffix = buff_fname + "_" + str(i/diff+1) + "_SUB.png"
makeCL(plt, tau_list[i:end], cn_list[:,i:end], un_list, path, suffix)

