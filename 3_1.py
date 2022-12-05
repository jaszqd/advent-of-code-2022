# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:06:14 2022

@author: scott
"""
import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

f = open("input_3.txt","r")

common_letters, container, rucksacks = [], [], []
priority = 0

#Including rstrip to remove trailing newline characters on certain elements.
#Not sure why it's including them on some parts when it shows the list but not
#the individual elements
for i in f.readlines():
    rucksacks.append(i.rstrip("\n"))

for rucksack in rucksacks:
    compartment_1 = rucksack[:int(len(rucksack)/2)]
    compartment_2 = rucksack[int(len(rucksack)/2):]
    for i in compartment_1:
        if i in compartment_2:
            common_letters.append(i)
            break

for letter in common_letters:
    if letter.isupper() == True:
        priority += uppercase.index(letter) + 27
    else:
        priority += lowercase.index(letter) + 1
        
print(common_letters)
print(priority)