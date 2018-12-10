#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

array1 = np.ones(30)
array_all = array1.reshape((3, 10))

print "len(array_all)    : %d" % len(array_all)
print "len(array_all[0]) : %d" % len(array_all[0])
print "len(array_all[1]) : %d" % len(array_all[1])
print "len(array_all[2]) : %d" % len(array_all[2])
print array_all
