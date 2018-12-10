#! /usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

# @Format
# first  : start
# second : end
# third  : diff
# @ret : axis?
x = np.arange(0, 10, 0.1)

# Exponential function
# @para : axis variable
y = np.exp(x)

# Set X and Y axes.
plt.plot(x, y)

# Set graph title
plt.title("Exponential Function : $ y = e^x $")

# Set range of Y axis.
plt.ylim(0, 5000)

plt.show()
