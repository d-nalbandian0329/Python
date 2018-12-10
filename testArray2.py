#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

array = np.zeros(10)
print array[2:5]

beta  = np.arange(0.0,10.0,0.1)
alpha = np.arange(0.0,10.0,0.1)

X,Y = np.meshgrid(beta, alpha)
 
print "X"
print X
print "Y"
print Y

data_list = np.random.rand(100,100)
plt.pcolormesh(X,Y,data_list)
plt.colorbar()

plt.xlim(0.0,9.0)
plt.ylim(0.0,9.0)

plt.show()
