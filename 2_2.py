# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 11:50:05 2022

@author: scott
"""

#Advent of Code Day 2_2
f = open("input_2.txt","r")

score = 0
strategy = []

#convert each entry to XYZ notation for ease of comparison
for match in f.readlines():
    strategy.append(match.split())

for match in strategy:
    print(match)
    if match[1] == "X":
        #LOSE
        if match[0] == "A":
            #LOSE AGAINST ROCK
            score += 3
        elif match[0] == "B":
            #LOSE AGAINST PAPER
            score += 1
        else:
            #LOSE AGAINST SCISSORS
            score += 2
    elif match[1] == "Y":
        #DRAW
        if match[0] == "A":
            score += 4
        elif match[0] == "B":
            score += 5
        else:
            score += 6
    else:
        if match[0] == "A":
            #WIN AGAINST ROCK
            score += 8
        elif match[0] == "B":
            #WIN AGAINST PAPER
            score += 9
        else:
            #WIN AGAINST SCISSORS
            score += 7

print(score)