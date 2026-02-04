f = open('input.txt', 'r')
ans = 0
for line in f:
    print(line)
    top = line.split(':')
    game = top[1].split(';')
    rmax, gmax, bmax = (0,0,0)
    for round in game:
        print(round)
        if 'red' in round:
            x = round.index('red')
            if int(round[x-3:x-1]) > rmax: rmax = int(round[x-3:x-1])
        if 'green' in round:
            x = round.index('green')
            if int(round[x-3:x-1]) > gmax: gmax = int(round[x-3:x-1])
        if 'blue' in round:
            x = round.index('blue')
            if int(round[x-3:x-1]) > bmax: bmax = int(round[x-3:x-1])
    power = rmax*gmax*bmax
    ans = ans + power
print(ans)
f.close()

