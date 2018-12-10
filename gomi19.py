#! /usr/bin/python
# -*- coding: utf-8 -*-

#import matplotlib
#matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

import random

'''
def makeLine(i, j, xmax, ymin, ymax):
  if(((i+1)<=xmax)and((j-1)>=ymin)and((j+1)<=ymax)):
    makeLine(i+1, j-1, xmax, ymin, ymax)

  plt.plot([i,j], [i+1,j-1])
  plt.plot([i,j], [i+1,j+1])

  if(((i+1)<=xmax)and((j-1)>=ymin)and((j+1)<=ymax)):
    makeLine(i+1, j+1, xmax, ymin, ymax)
'''

xlist = []
ylist = []
for i in range(0, 31):
  xlist.append(i)
  ylist.append(i)

i = 0
while i < len(xlist):
  j = 0
  while j < len(ylist):
    plt.plot(xlist[i], ylist[j], "ro")
    j += 1
  i += 1

#makeLine(0, len(ylist)/2, len(xlist)-1, 0, len(ylist)-1)

i = 15
j = 15
#test_list = []
#test_list.append(j)

while (i+1)<len(xlist) and (j-1)>0 and (j+1)<len(ylist):
  flag = random.randint(0, 1)
  x = i
  y = j

  if(flag == 0):
    j -= 1
  else:
    j += 1

  i += 1
  plt.plot([x,y], [i,j], color="r",linestyle="-")




'''
xlist2 = []
for n in range(len(test_list)):
  xlist2.append(n)
plt.plot(xlist2, test_list)
'''
"""
X = np.random.rand(2)
Y = np.random.rand(2)

plt.plot(X,Y,"-o")
"""
plt.show()
