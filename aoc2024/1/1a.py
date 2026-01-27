list1 = []
list2 = []
sum = 0
f = open('input.txt', 'r')
for i in f:
    line_list = i.split()
    list1.append(int(line_list[0]))
    list2.append(int(line_list[1]))
list1 = sorted(list1)
list2 = sorted(list2)
for i in range(len(list1)):
    sum += abs(list1[i]-list2[i])
print(sum)
