dial = 50
count = 0

for line in open("test.txt"):
    print(count, dial, line.strip("\n"))
    if line.find("L") == 0:
        pass
    else:
        pass
    
print(count)
