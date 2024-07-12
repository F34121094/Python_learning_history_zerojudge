read = input()
l = len(read)
for i in range(l):
    k = i
    for j in range(l):
        if k > l-1 : k = 0
        print(read[k],end = '')
        k += 1
    print()
