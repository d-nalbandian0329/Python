#! /usr/bin/python

import numpy as np

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

xmin, xmax = -np.pi, np.pi

x = np.arange(xmin, xmax, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# sin plot
plt.subplot(2, 1, 1)
plt.plot(x, y_sin)
plt.title("$\sin x$")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

# cos plot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title("$\cos x$")
plt.xlim(xmin, xmax)
plt.ylim(-1.3, 1.3)

# Avoid to duplicate graphtitle
plt.tight_layout()

plt.show()

plt.savefig("/Users/iwaitoshiya/Desktop/graph.png")
