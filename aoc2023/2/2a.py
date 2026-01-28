# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 21:59:24 2023

@author: Kyle
"""

# sum of game IDs possible with 12 red, 13 green, 14 blue
# not 2545

f = open('input.txt', 'r')
ans = 0
gameGood = None
for line in f:
    print(line)
    top = line.split(':')
    game = top[1].split(';')
    rcheck, bcheck, gcheck = (True, True, True)
    for round in game:
        print(round)
        if 'red' in round:
            x = round.index('red')
            if int(round[x-3:x-1]) > 12: rcheck = False
        if 'green' in round:
            x = round.index('green')
            if int(round[x-3:x-1]) > 13: bcheck = False
        if 'blue' in round:
            x = round.index('blue')
            if int(round[x-3:x-1]) > 14: gcheck = False
        if not(rcheck and bcheck and gcheck):
            gameGood = False
    if gameGood != False:
        if top[0][-3] == '1': ans = ans + 100
        else: ans = ans + int(top[0][-2:])
    else: gameGood = None
    print(ans, gameGood)
print(ans)

