# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:00:22 2022

@author: scott
"""

f = open("input_4.txt","r")

assignments, container = [], []
count = 0

for i in f.readlines():
    assignments.append(i.rstrip("\n").split(","))

#print(assignments)

for assignment in assignments:
    shift1, shift2,range1, range2 = [], [], [], []
    shift1.append(assignment[0].split("-"))
    shift2.append(assignment[1].split("-"))
    range1 = list(range(int(shift1[0][0]), int(shift1[0][1])+1))
    range2 = list(range(int(shift2[0][0]), int(shift2[0][1])+1))
    if len(range2) > len(range1):
        for element in range1:
            if element in range2:
                count += 1
                break
    else:
        for element in range2:
            if element in range1:
                count += 1
                break

print(count)