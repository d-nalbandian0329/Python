#! /usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

import csv


plt.plot([50,60], [50,70], "r-", alpha=0.1)
plt.plot([50,60], [50,30], "r-",alpha=0.1)
plt.plot([60,70], [70,80], "r-",alpha=0.7)
plt.plot([60,70], [70,60], "r-",alpha=0.8)

plt.plot([70,80], [80,85], "r-",alpha=0.8)
plt.plot([70,80], [80,75], "r-",alpha=0.2)
plt.plot([70,80], [60,65], "r-",alpha=0.3)
plt.plot([70,80], [60,55], "r-",alpha=0.9)

plt.show()
