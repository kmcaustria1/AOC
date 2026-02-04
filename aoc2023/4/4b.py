#TODO, no hardcode, one run
#10, 25, 40, 212
#5, 8, 23, 6

left = 10
right = 25
split = 40
length = 212

sum = 0
leftnums = []
rightnums = []

scratch = []
for i in range(length):
    scratch.append(1)

for line in open("input.txt"):
#    split = line.find('|')
#    print(split)
    leftline = []
    for i in range(left):
        leftline.append(int(line[split-3-(3*i):split-1-(3*i)]))
    leftnums.append(leftline)

    rightline = []
    for i in range(right):
        rightline.append(int(line[split+2+(3*i):split+4+(3*i)]))
    rightnums.append(rightline)

for index, day in enumerate(leftnums):
    mynums = rightnums[index]
    hits = 0
    for win in day:
        for num in mynums:
            if win == num:
                hits += 1
    for i in range(index+1, index+hits+1):
        scratch[i] += scratch[index]

for cards in scratch:
    sum += cards
print(sum)
