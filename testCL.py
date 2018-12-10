#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

fig,ax = plt.subplots()


X,Y = np.meshgrid(np.arange(0, 101, 1), np.arange(0, 101, 1))

Z = np.random.rand(101, 101)/5


plt.xlim(1, 100)
plt.ylim(1, 100)

val = np.linspace(0.0, 1.0, 20, endpoint = True)

plt.contour(X, Y, Z, val)
nn = plt.contourf(X, Y, Z, val)
hoge = plt.colorbar(nn, ticks = val)

plt.show()

