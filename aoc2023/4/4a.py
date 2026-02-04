#TODO, no hardcode, one run

left = 10
right = 25
leftnums = []
rightnums = []
sum = 0

for line in open("input.txt"):
    split = line.find('|')
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
    day_wins = 0
    for win in day:
        for num in mynums:
            if win == num:
                if not day_wins:
                    day_wins = 1
                else:
                    day_wins *= 2
    sum += day_wins

print(sum)
