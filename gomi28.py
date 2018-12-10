#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

w = np.arange(1, 100, 1)
x = np.arange(1, 100, 1)
y = np.arange(1, 100, 1)
z = np.arange(1, 100, 1)

ary = np.array([a*b*c*d for a in w for b in x for c in y for d in z])

print ary

"""
bias = 0
for i in np.arange(9):
  print ary[bias:bias+9]
  bias += 9
"""
