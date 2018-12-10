#! /usr/bin/python

import matplotlib.pyplot as plt

plt.plot([3, 1, 4, 1, 5, 9, 2, 6, 5], label = "Data1")
plt.plot([3, 5, 8, 9, 7, 9, 3, 2, 3], label = "Data2")
# Print legend.
plt.legend()

plt.title("Graph Title")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
