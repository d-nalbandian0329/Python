#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

xmin, xmax = -np.pi*2, np.pi*2

x1 = np.arange(xmin, xmax, 0.1)
y1 = np.sin(x1)
plt.xlim(xmin, xmax)
plt.ylim(-1.2, 1.2)
plt.plot(x1, y1)
plt.savefig("/Users/iwaitoshiya/Desktop/g1_1.png")

plt.figure()

x2 = np.arange(xmin, xmax, 0.1)
y2 = np.cos(x2)
plt.xlim(xmin, xmax)
plt.ylim(-1.2, 1.2)
plt.plot(x2, y2)
plt.savefig("/Users/iwaitoshiya/Desktop/g1_2.png")
