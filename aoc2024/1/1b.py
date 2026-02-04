list1 = []
list2 = []
sum = 0
f = open('input.txt', 'r')
for i in f:
    line_list = i.split()
    list1.append(int(line_list[0]))
    list2.append(int(line_list[1]))
for i in list1:
    temp = list2.count(i)
    print(i,temp)
    sum += int(i)*temp
print(sum)
f.close()
