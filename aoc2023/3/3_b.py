#assumes input lines 141 chars long
symbols = []
numbers = []
tempArr = []
sum = 0
f = open('input.txt', 'r')

for line in f:
    line_syms = []
    line_nums = []
    index = 0
    #print(len(line))
    while index < len(line)-1:
        if line[index].isnumeric():
            if line[index+1].isnumeric():
                if line[index+2].isnumeric():
                    line_nums.append((int(line[index:index+3]), index, index+2))
                    index += 2
                else:
                    line_nums.append((int(line[index:index+2]), index, index+1))
                    index += 1
            else:
                line_nums.append((int(line[index]), index, index))
        elif line[index] == '*': line_syms.append(index)
        index += 1
    symbols.append(line_syms)
    numbers.append(line_nums)

#print(symbols)

for sym in symbols[0]:
    if sym == 0: left = 0
    else: left = sym-1
    if sym == 140: right = 140
    else: right = sym+1
    tempArr.clear()

    for index, num in enumerate(numbers[0]):
        if left == num[2] or right == num[1]:
            tempArr.append(num[0])

    for index, num in enumerate(numbers[1]):
        if num[1] >= left and num[1] <= right:
            tempArr.append(num[0])
        elif num[2] >= left and num[2] <= right:
            tempArr.append(num[0])

    if len(tempArr) == 2:
        sum += tempArr[0]*tempArr[1]

for i in range(1,len(symbols)-1):
    for sym in symbols[i]:
        if sym!= None:
            if sym == 0: left = 0
            else: left = sym-1
            if sym == 140: right = 140
            else: right = sym+1
            tempArr.clear()
            for index, num in enumerate(numbers[i-1]):
                if num[1] >= left and num[1] <= right:
                    tempArr.append(num[0])
                elif num[2] >= left and num[2] <= right:
                    tempArr.append(num[0])

            for index, num in enumerate(numbers[i]):
                if left == num[2] or right == num[1]:
                    tempArr.append(num[0])

            for index, num in enumerate(numbers[i+1]):
                if num[1] >= left and num[1] <= right:
                    tempArr.append(num[0])
                elif num[2] >= left and num[2] <= right:
                    tempArr.append(num[0])
        
            if len(tempArr) == 2:
                sum += tempArr[0]*tempArr[1]

for sym in symbols[len(symbols)-1]:
    if sym == 0: left = 0
    else: left = sym-1
    if sym == 140: right = 140
    else: right = sym+1
    tempArr.clear()
    for index, num in enumerate(numbers[len(symbols)-2]):
        if num[1] >= left and num[1] <= right:
            tempArr.append(num[0])
        elif num[2] >= left and num[2] <= right:
            tempArr.append(num[0])

    for index, num in enumerate(numbers[len(symbols)-1]):
        if left == num[2] or right == num[1]:
            tempArr.append(num[0])

    if len(tempArr) == 2:
        sum += tempArr[0]*tempArr[1]

print(sum)
f.close()
