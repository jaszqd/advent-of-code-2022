# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:33:56 2022

@author: scott
"""

f = open("testinput_4.txt","r")

assignments, container = [], []
count = 0

for i in f.readlines():
    assignments.append(i.rstrip("\n").split(","))

#print(assignments)

for assignment in assignments:
    shift1, shift2,range1, range2 = [], [], [], []
    shift1.append(assignment[0].split("-"))
    shift2.append(assignment[1].split("-"))
    range1 = set(range(int(shift1[0][0]), int(shift1[0][1])+1))
    range2 = set(range(int(shift2[0][0]), int(shift2[0][1])+1))
    if range1.issubset(range2) == True or range2.issubset(range1) == True:
        print("yee")
        count += 1
    else:
        print("haw")
        continue

print(count)