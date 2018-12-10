#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# X range is from -PI to +PI.
xmin, xmax = -np.pi, np.pi


x = np.arange(xmin, xmax, 0.1)

y_sin = np.sin(x)

y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)

# Draw dashed line at y=-1,y=1.
plt.hlines([-1, 1], xmin, xmax, linestyle = "dashed")

plt.title(r"$\sin(x)$ and $\cos(x)$")

plt.xlim(xmin, xmax)

plt.ylim(-1.3, 1.3)

plt.show()
