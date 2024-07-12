while True:
    n = int(input())
    arr = [0 for i in range(n)]
    for i in range(len(arr)):
        arr[i] = str(i+1)
    # print(arr)
    a = ''.join(arr)
    # print(a)
    num = int(a)