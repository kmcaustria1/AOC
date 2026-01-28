sum = 0
f = open('input.txt', 'r')
for line in f:
    report = line.split()
    report = list(map(int, report))
    check = 1
    hit1 = 0
    hit2 = 0
    if report == sorted(report) or report == sorted(report, reverse = True):
        for i in range(len(report)-1):
            if abs(report[i]-report[i+1]) < 4 and abs(report[i]-report[i+1]) > 0:
                continue
            else:
                if hit1 == 0: hit1 = i
                elif hit2 == 0 and hit1 == i-1:
                    if abs(report[i-1]-report[i+1]) < 4 and abs(report[i-1]-report[i+1]) > 0:
                        hit2 = 1
                    else:
                        check = 0
                        break
                else:
                    check = 0
                    break
        sum += check
        
print(sum)

#686, 723, 639, 799, 627
