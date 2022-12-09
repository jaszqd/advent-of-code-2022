# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 21:29:35 2022

@author: scott
"""


f = open("input_6.txt","r")

datastream = str(f.read())

count = 0

day1 = 4
day2 = 14

for count, value in enumerate(datastream):
    key = datastream[count:(count+day2)]
    print(key)
    container = []
    for keycount, keyvalue in enumerate(key):
        tally = key.count(keyvalue)
        container.append(tally)
    if sum(container) == day2:
        print(count + day2)
        break
    else:
        continue