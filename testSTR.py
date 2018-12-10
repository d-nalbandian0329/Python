#! /usr/bin/python
# -*- coding: utf-8 -*-

str = "LN50DX0.100ALPHA0.500BETA0.500CN10.csv"

start = str.index("BETA")
end   = str.index("CN");

start += 4

print str
print start
print end

beta = ""
for idx in range(start, end):
  beta += str[idx]

print beta
print float(beta)
