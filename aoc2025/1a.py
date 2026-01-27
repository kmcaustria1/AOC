dial = 50
count = 0

for line in open("test.txt"):
    #print(count, dial, line.strip("\n"))
    if line.find("L") == 0:
        temp = dial - int(line.lstrip("LR"))
        if temp < 0: dial = 100 - (-temp%100)
        else: dial = temp
    else: dial = dial + int(line.lstrip("LR"))
    dial = dial%100
    if dial == 0: count += 1

#print(dial)    
print(count)