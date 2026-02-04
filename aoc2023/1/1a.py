# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 20:00:32 2023

@author: Kyle
"""

f = open('input.txt', 'r')
ans = 0
for i in f:
    front = ''
    back = ''
    for j in i:
        if j.isdigit():
            front = j
    for j in reversed(i):
        if j.isdigit():
            back = j
    midsum = back + front
    midsum = int(midsum)
    ans = midsum + ans
print(ans)
f.close()

