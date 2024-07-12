from collections import Counter
while 1:
    try:
        n = int(input())
        arr = [int(i) for i in input().split()]
        a = Counter(arr)
        c,b = [],[]
        for key in a:
            b.append(a[key])
        m =max(b)
        for key in a:
            if a[key] == m:
                c.append(key)
        c.sort()
        for i in c:
            print(f'{i} {m}')
    except:
        break


