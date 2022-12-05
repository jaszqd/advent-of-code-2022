# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:48:42 2022

@author: scott
"""
import string

lowercase = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

f = open("input_3.txt","r")

rucksacks = []
priority = 0

#Including rstrip to remove trailing newline characters on certain elements.
#Not sure why it's including them on some parts when it shows the list but not
#the individual elements
for i in f.readlines():
    rucksacks.append(i.rstrip("\n"))

count = 0
container = []
for rucksack in rucksacks:
    container.append(rucksack)
    count += 1
    print(count)
    if count == 3:
        print(container)
        for letter in container[0]:
            if letter in container[1]:
                if letter in container[2]:
                    if letter.isupper() == True:
                        priority += uppercase.index(letter) + 27
                        container = []
                        count = 0
                        break
                    else:
                        priority += lowercase.index(letter) + 1
                        container = []
                        count = 0
                        break

print(priority)