#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(30)
y = np.sin(x) + np.random.randn(30)
plt.plot(x, y, "o")
plt.show()
