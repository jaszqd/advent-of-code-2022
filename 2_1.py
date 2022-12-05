# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:15:36 2022

@author: scott
"""
#Advent of Code Day 2_1
f = open("input_2.txt","r")

score = 0
strategy = []

#convert each entry to XYZ notation for ease of comparison
for match in f.readlines():
    strategy.append(match.replace("A","X").replace("B","Y").replace("C","Z").split())

for match in strategy:
    #Draw scenario
    if match[0] == match[1]:
        #Draw
        score += 3
        if match[1] == "X":
            score += 1
        elif match[1] == "Y":
            score += 2
        else:
            score += 3
    else:
        #Rock W/L scenario
        if match[1] == "X":
            if match[0] == "Y":
                #Loss
                score += 1
            else:
                #Win
                score += 7
        #Paper W/L scenario
        elif match[1] == "Y":
            if match[0] == "X":
                #Win
                score += 8
            else:
                #Loss
                score += 2
        #Scissors W/L scenario
        elif match[1] == "Z":
            if match[0] == "X":
                #Loss
                score += 3
            else:
                #Win
                score += 9

print(score)

