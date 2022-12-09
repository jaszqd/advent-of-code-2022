# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:43:13 2022

@author: scott
"""
import itertools
import re
from parse import *
from parse import compile

f = open("input_5.txt","r")

crates, instructions, stack, parsed_instructions = [], [], [], []

#Modify strings, then traverse and append
#The replaces are to get everything in a consistent format so that each row has
#a length of five before the transpose
#Issue here with crates
for line in f.readlines():
    container = []
    line = line.rstrip("\n").replace("["," ").replace("]"," ")
    if "move" not in line:
        if line != "":
            for i in line:
                container.append(i)
        crates.append(container)
    else:
        instructions.append(line)

#this removes leading and trailing white space for easier comparison to the stack
crates[-1] = crates[-1][1:-1]

trans_crates = list(map(list, itertools.zip_longest(*crates, fillvalue=" ")))

#print(trans_crates)

#Leaving crates in reverse order because I can just index to the list that I need
#Crate transpose issue was due to removing certain string elements too early
for crate in trans_crates:
    if crate[-1] == " ":
        trans_crates.remove(crate)
for crate in trans_crates:
    if " " in crate:
        while " " in crate:
            crate.remove(" ")

while [] in trans_crates:
    trans_crates.remove([])

for crate in trans_crates:
    for i in crate:
        if i.isnumeric():
            crate.remove(i)

#Could probably just use a second compiler in the parse library after converting 
#the return to a string

p = compile("move {} from {} to {}")

#Convert plain text instructions to numerical instructions in the form of 
#a list with three ints indicating the amount of crates to move, then the 
#start column and then the final column
for line in instructions:
    container = []
    line = str(p.parse(line))
    #regex expression collects everything from the tuple returned by the parser
    regex = re.compile(r'(?<=\()(.*?)(?=\))')
    value = regex.search(line)
    line = value.group(1)
    for i in line.split(","):
        container.append(int(i.replace("'","").replace(",","").replace(" ","")))
    parsed_instructions.append(container)

#This block of code adds the number of crates specified by the instructions 
#to an empty list and then "moves" the crates by using list slicing 
#to add the crate stack to the front of the proper stack specified
for line in parsed_instructions:
    value = line[0]
    if trans_crates[(int(line[1])-1)] != None:
        crate_stack = trans_crates[(line[1])-1][:value]
        for crate in crate_stack:
            trans_crates[(line[1])-1].remove(crate)
        trans_crates[int(line[2])-1][0:0] = crate_stack
    else:
        continue


#Collects top crates from list
def topcrates(cratelist):
    top_crates = []
    for stack in cratelist:
        for crate in stack:
            if crate != " ":
                top_crates.append(crate)
                break
    return top_crates

print(topcrates(trans_crates))