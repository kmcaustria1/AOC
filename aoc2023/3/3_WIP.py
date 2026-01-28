# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 21:37:27 2024

@author: Kyle
"""

def findNumL(value, loc, num = 0):
    if value[loc-1].isnumeric():
        findNumL(value, loc-1, num+1)
    else: return num
    

def findNumR(value, loc, num = 0):
    if value[loc+1].isnumeric():
        findNumL(value, loc+1, num+1)
    else: return num
    

f = open('test.txt', 'r')
row = 0
symbols = []
nextline = []
total = 0
lastRow = 0

for i in f:
    for j in range(len(i)):
        if i[j].isnumeric() or i[j] == '.' or i[j] == '\n':
            continue
        symbols.append((row,j,0))
    row += 1
    lastRow +=1


f.seek(0)

for row,value in enumerate(f):
    while symbols:
        if symbols[0][0] > row:
            for i in nextline: symbols.insert(0,i)
            nextline.clear()
            break
        locTuple = symbols.pop(0)
        print(row, value, locTuple, total)
        if locTuple[2] == 1:
            temp = []
            lNumOffset = findNumL(value, locTuple[1])
            rNumOffset = findNumR(value, locTuple[1])
            if lNumOffset: temp.append(value[locTuple[1]-lNumOffset,locTuple[1]])
            if value[locTuple[1]].isnumeric(): temp.append(value[locTuple[1]])
            if rNumOffset: temp.append(value[locTuple[1],locTuple[1]+rNumOffset])
            tempstr = ''
            if temp:
                for i in temp:
                    tempstr += i
                total += int(tempstr)
        else:
            nextline.append((locTuple[0]+1,locTuple[1], 1))
            lNumOffset = findNumL(value, locTuple[1])
            rNumOffset = findNumR(value, locTuple[1])
            if lNumOffset: total += int(value[locTuple[1]-lNumOffset,locTuple[1]])
            if rNumOffset: total += int(value[locTuple[1],locTuple[1]+rNumOffset])
            

 
