#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

# Extract parameter from CSV-filename.
def extractPARA(str, s1, s2):
  start = str.index(s1) + len(s1)
  end   = str.index(s2)

  buff=""
  for i in range(start, end, 1):
    buff += str[i]

  return buff

argv = sys.argv

num = len(argv)
print "num : %d" % num
list = [(extractPARA(x, "CN", ".csv"), x) for x in argv[1:num]]

for e in list:
  print e[0] + ", " + e[1]

