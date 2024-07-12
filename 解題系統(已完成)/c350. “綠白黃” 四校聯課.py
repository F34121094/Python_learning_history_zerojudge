a,b,c = map(int,input().split())
total = 0
if b > a:
    print(a)
else:
    while a > 0:
        if a >= b:
            total += b
            a -= b
            a += c
        else:
            total += a
            a -= a
    print(total)