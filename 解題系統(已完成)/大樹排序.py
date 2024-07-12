from sys import stdin

for n in stdin:
    n = int(n)
    arr = []
    for i in range(n):
        arr.append(int(input()))
    sort_arr = sorted(arr)
    for i in range(len(sort_arr)):
        print(sort_arr[i])

