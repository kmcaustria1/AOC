seeds = []
s2soil = []
s2fer = []
f2wat = []
w2lig = []
l2tem = []
t2hum = []
h2loc = []
lowest = 2**63 - 1
#TODO be less naive

def parse(array):
    line = f.readline().split()
    line = [int(x) for x in line]
    array.append(line)
    line = f.readline().split()
    while line != []:
        line = [int(x) for x in line]
        index = 0
        while index < len(array):
            if line[0] < array[index][0]:
                array.insert(index, line)
                break
            else:
                index += 1
        if index == len(array):
            array.append(line)
        line = f.readline().split()

def map2(array, num):
    out = None
    for line in array:
        if num >= line[1] and num < line[1]+line[2]:
            out = line[0] + num - line[1]
            return out
    return num

f = open('input.txt', 'r')
while 1:
    line = f.readline().split()
    if line[0] == 'seeds:':
        for i in range(1,len(line),2):
            seeds.append([int(line[i]),int(line[i])+int(line[i+1])])
        f.readline()
    elif line[0] == 'seed-to-soil':
        parse(s2soil)
    elif line[0] == 'soil-to-fertilizer':
        parse(s2fer)
    elif line[0] == 'fertilizer-to-water':
        parse(f2wat)
    elif line[0] == 'water-to-light':
        parse(w2lig)
    elif line[0] == 'light-to-temperature':
        parse(l2tem)
    elif line[0] == 'temperature-to-humidity':
        parse(t2hum)
    elif line[0] == 'humidity-to-location':
        parse(h2loc)
        break
f.close()

for seed_range in seeds:
    for seed in range(seed_range[0],seed_range[1]):
        this = map2(h2loc, map2(t2hum, map2(l2tem, map2(w2lig, map2(f2wat, map2(s2fer, map2(s2soil, seed)))))))
        if this < lowest: lowest = this
print(lowest)
    
