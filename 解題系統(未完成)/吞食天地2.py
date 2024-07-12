from sys import stdin
for n in stdin:
    a,b = map(int,n.rstrip().split())
    arr_a = [[0 for i in range(a)]]

    for i in range(a):
        arr_a.append([int(_) for _ in stdin.readline().split()])
        arr_a[i] = [0] + arr_a[i]
    arr_a[a] = [0] + arr_a[a]

    for i in range(a+1):
        arr_a[i] = list(accumulate(arr_a[i]))

    for i in range(1,a+1):
        arr_a[i] = [x+y for x,y in zip(arr_a[i],arr_a[i-1])]

    for k in range(b):
        arr_b = list(map(int, stdin.readline().rstrip().split()))
        total = arr_a[arr_b[2]][arr_b[3]] + arr_a[arr_b[0]-1][arr_b[1]-1] - arr_a[arr_b[2]][arr_b[1]-1] - arr_a[arr_b[3]][arr_b[0]-1]
        print(total)

