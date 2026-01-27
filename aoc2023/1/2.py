# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:38:17 2023

@author: Kyle
"""
#reverse check for backwards traversal (rouf,...)

f = open('input.txt','r')
total = 0

for i in f:
    length = len(i)-1
    i = i + '----'
        
    j = 0
    first = ''
    last = ''
    
    while not first:
        if i[j].isnumeric():
            first = i[j]
        elif i[j] == 't':
            if i[j+1:j+3]== 'wo':
                first = '2'
            elif i[j+1:j+5]== 'hree':
                first = '3'
            else: j+=1
        elif i[j] == 'f':
            if i[j+1:j+4]== 'our':
                first = '4'
            elif i[j+1:j+4]== 'ive':
                first = '5'
            else: j+=1
        elif i[j] == 's':
            if i[j+1:j+3]== 'ix':
                first = '6'
            elif i[j+1:j+5]== 'even':
                first = '7'
            else: j+=1
        elif i[j] == 'o':
            if i[j+1:j+3] == 'ne':
                first = '1'
            else: j+=1
        elif i[j] == 'e':
            if i[j+1:j+5] == 'ight':
                first = '8'
            else: j+=1
        elif i[j] == 'n':
            if i[j+1:j+4] == 'ine':
                first = '9'
            else: j+=1
        else: j+=1

    j = length
    while not last:
        if i[j].isnumeric():
            last = i[j]
        elif i[j] == 't':
            if i[j+1:j+3]== 'wo':
                last = '2'
            elif i[j+1:j+5]== 'hree':
                last = '3'
            else: j-=1
        elif i[j] == 'f':
            if i[j+1:j+4]== 'our':
                last = '4'
            elif i[j+1:j+4]== 'ive':
                last = '5'
            else: j-=1
        elif i[j] == 's':
            if i[j+1:j+3]== 'ix':
                last = '6'
            elif i[j+1:j+5]== 'even':
                last = '7'
            else: j-=1
        elif i[j] == 'o':
            if i[j+1:j+3] == 'ne':
                last = '1'
            else: j-=1
        elif i[j] == 'e':
            if i[j+1:j+5] == 'ight':
                last = '8'
            else: j-=1
        elif i[j] == 'n':
            if i[j+1:j+4] == 'ine':
                last = '9'
            else: j-=1
        else: j-=1      

    total = total + (int(first+last))
    first = ''
    last = ''
    
print(total)