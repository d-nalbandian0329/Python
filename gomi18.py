#! /usr/bin/python
# -*- coding: utf-8 -*-

import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

plt.plot([6, 2], [3, 9])
plt.plot([9, 9], [1, 1])

plt.savefig("/Users/iwaitoshiya/Desktop/testGP.png")
plt.show()
