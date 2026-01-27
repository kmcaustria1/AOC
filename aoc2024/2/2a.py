sum = 0
f = open('input.txt', 'r')
for line in f:
    report = line.split()
    report = list(map(int, report))
    check = 1
    if report == sorted(report) or report == sorted(report, reverse = True):
        for i in range(len(report)-1):
            if abs(report[i]-report[i+1]) < 4 and abs(report[i]-report[i+1]) > 0:
                continue
            else: 
                check = 0
                break
        sum += check
        
print(sum)
