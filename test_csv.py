#! /usr/bin/python
# -*- coding: utf-8 -*-

import csv

if __name__ == "__main__":
  fname = "/Users/iwaitoshiya/Desktop/test_csv.csv"

  data_list = []

  with open(fname, "r") as f:
    reader = csv.reader(f)
    for data in reader:
      data_list.append(data)

  for i in range(len(data_list)):
    print data_list[i]

  NUM = int(data_list[0][0])
  LAY = int(data_list[1][0])
  CN  = int(data_list[2][0])

  print "NUM = %d" % NUM
  print "LAY = %d" % LAY
  print "CN  = %d" % CN

  print data_list[5][2]
