#! bin/usr/python

import numpy as np
import matplotlib.pyplot as plt

# Generate 100*100 matrix
plt.imshow(np.random.randn(100, 100))
plt.title("100x100 matrix")
plt.show()
