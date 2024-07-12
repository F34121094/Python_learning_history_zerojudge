from sys import stdin

for read in stdin:
    a,b = map(int,read.rstrip().split())
    arr = []
    for i in range(a):
        arr.append([int(x) for x in input().split()])
    # print(arr)
    for i in range(b):
         for time in arr:
             print(time[i],end = " ")
         print()