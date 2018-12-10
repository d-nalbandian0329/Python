#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

import matplotlib.font_manager
fontprop = matplotlib.font_manager.FontProperties(fname="Library/Fonts/fonts-japanese-gothic.ttf")


x = np.linspace(-20, 20, 800)

# y = pow(x, 2);
y = (x**2)

plt.plot(x, y)

plt.savefig("/Users/iwaitoshiya/Desktop/graph3.png")

plt.show()
