#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path

import csv
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


argv = sys.argv
if (len(argv) < 3):
  print "Too few data!!"
  quit()

fname      = argv[1]
stack_path = argv[2]

list = []
with open(fname, "r") as f:
  data_list = csv.reader(f)
  for data in data_list:
    list.append(data)

array = np.array(list)

base = os.path.basename(fname)

alpha = float(extractPARA(base, "ALPHA", "BETA"))
beta  = float(extractPARA(base, "BETA", "CN"))
sigma = float(extractPARA(base, "SIGMA", ".csv"))
ln    = int(extractPARA(base, "LN", "DX"))
cn    = int(extractPARA(base, "CN", "SIGMA"))


diff = 0.02

buff = ""
target = int(sigma/cn/diff)*diff
for i in range(len(array)):
  if (target==float(array[i][0])):
    buff = array[i][1]
    break

stack_path += "SIGMA_CN_LN%d.csv" % ln
with open(stack_path, "a") as f:
  f.write("%f,%f,%f\n" % (alpha, beta, float(buff)))
