#! /usr/bin/python
# CSV module test.

import csv

with open("/Users/iwaitoshiya/Desktop/u226136_NeuronalAvalanchesData/CSV/Test/testCN4_sigma_f.csv", "r") as f:
  reader = csv.reader(f)

  csv_list = []
  for data in reader:
    csv_list.append(data)

diff    = float(csv_list[1][0]) - float(csv_list[0][0])
counter = float(csv_list[0][0])
end     = float(csv_list[len(csv_list)-1][0]) + diff/4

while counter <= end:
  print counter
  counter += diff
