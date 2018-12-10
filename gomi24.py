#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib.font_manager
fontprop = matplotlib.font_manager.FontProperties(fname="Library/Fonts/fonts-japanese-gothic.ttf")

import numpy as np
import matplotlib.pyplot as plt

# About this distribution.
# Mean : 0
# Standard Deviation : 1
data = np.random.normal(0, 1, 10000)

plt.hist(data, bins=40, range=(-5, 5))
plt.xlabel("TEST [ x${10^3}$ ]")
plt.show()
