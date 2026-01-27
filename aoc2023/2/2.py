# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:59:24 2023

@author: Kyle
"""

f = open('input.txt', 'r')
ans = 0
for i in f:
    top = i.split(':')
    sets = top[1].split(';')
    rcheck, bcheck, gcheck = (1,1,1)
    for j in sets:
        if 'red' in j:
            x = j.index('red')
            if int(j[x-3:x-1]) > 12: rcheck = False
        if 'blue' in j:
            x = j.index('blue')
            if int(j[x-3:x-1]) > 13: bcheck = False
        if 'green' in j:
            x = j.index('green')
            if int(j[x-3:x-1]) > 14: gcheck = False
        print(rcheck, bcheck, gcheck)
        if not(rcheck and bcheck and gcheck): break
    else:
        if top[0][-3] == '1': ans = ans + 100
        else: ans = ans + int(top[0][-2:])
    print(ans,i)
print(ans)
