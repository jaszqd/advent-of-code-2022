# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:44:45 2022

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
#There's an error here regarding the crate transpose. After stack 4, it's fucked.
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

print(trans_crates)

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

#IndexError: pop from empty list??
for line in parsed_instructions:
    count = 0
    value = line[0]
    while count < value:
        if trans_crates[(int(line[1])-1)] != None:
            current_crate = trans_crates[(int(line[1])-1)].pop(0)
            trans_crates[(int(line[2])-1)].insert(0, current_crate)
            count += 1
        else:
            count += 1
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

