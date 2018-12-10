#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0.0, 1.0, 0.02)
y = np.arange(0, 100, 2)

plt.xlim(0.0,1.0)

plt.bar(x, y)
plt.show()
