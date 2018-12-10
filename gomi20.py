#! /usr/bin/python
# -*- coding: utf-8 -*-

#import matplotlib
#matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def test_plot():
  plt.plot([0,10], [0,57], "r")
  plt.plot([0,10], [0,29], "r")
  plt.plot([0,10], [0,16], "r")
  plt.plot([0,10], [0,28], "r")
  plt.plot([0,10], [0,118], "r")
  plt.plot([0,10], [0,196], "r")

  plt.plot([10,20], [57,47], "r")
  plt.plot([10,20], [57,67], "r")

  plt.plot([10,20], [29,19], "r")
  plt.plot([10,20], [29,39], "r")

  plt.plot([10,20], [16,6], "r")
  plt.plot([10,20], [16,26], "r")

  plt.plot([10,20], [28,18], "r")
  plt.plot([10,20], [28,38], "r")

  plt.plot([10,20], [118,108], "r")
  plt.plot([10,20], [118,128], "r")

  plt.plot([10,20], [196,186], "r")
  plt.plot([10,20], [196,206], "r")


if __name__ == "__main__":
  plt.xlim(0,200)
  plt.ylim(0,200)
  test_plot()
  plt.show()
