#task1
import random

N = int(input("Write the number of files:  "))
M = int(input("Write how much numbers will be in each file:  "))
maxNum = -99999999
Sum = 0
Sum1 = 0
newMax = -99999999
newMax2 = -99999999
for i in range(N):
    randomlist = random.sample(range(1, 100), M)
    f = open("/home/raissov/Desktop/python_file_create/numbers%s.txt" % i, "w").write(str(randomlist))

for i in range(N):
    f = open("/home/raissov/Desktop/python_file_create/numbers%s.txt" % i, "r")
    newList = f.read().strip('][').split(', ')
    for x in range(0, len(newList)):
        Sum = Sum + int(newList[x])
        int(newList[x])
        if newList[x] > newMax:
            newMax = newList[x]
    if Sum > maxNum:
        maxNum = Sum


for i in range(N):
    f = open("/home/raissov/Desktop/python_file_create/numbers%s.txt" % i, "r")
    newList = f.read().strip('][').split(', ')
    for x in range(0, len(newList)):
        Sum1 = Sum1 + int(newList[x])
        int(newList[x])
        if newList[x] > newMax2:
            newMax2 = newList[x]

    if Sum == Sum1:
        print("Maximum sum of the numbers (%s) in the file_N(numbers%s.txt)" % (Sum, i))

    if newMax == newMax2:
        print("Maximum  numbers maxNum (%s) in the file_N(numbers%s.txt)" % (newMax, i))

for i in range(N):
    f = open("/home/raissov/Desktop/python_file_create/numbers%s.txt" % i, "r")
    newList = f.read().strip('][').split(', ')
    for x in range(0, len(newList)):
        Sum1 = Sum1 + int(newList[x])

    print("file_N (%s) numbers are: " %i, newList, Sum1)


