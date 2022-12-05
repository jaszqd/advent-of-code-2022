# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:48:36 2022

@author: scott
"""
currentElf, caloriesList = [], []

f = open("input_1.txt","r")

for calorie in f.readlines():
    if calorie != "\n":
        currentElf.append(int(calorie))
    elif calorie == "\n":
        caloriesList.append(sum(currentElf))
        currentElf = []
caloriesList.append(sum(currentElf))

#Part 1 solution:
#print("Max Calories: " + str(max(caloriesList)), "\nElf Number: " + str(caloriesList.index(max(caloriesList))+1))

#Part 2 solution
caloriesList.sort(reverse = True)
print(caloriesList[:3], sum(caloriesList[:3]))