import math
a = int(input())
i = 2

while(a >= i):
    if a % i != 0 :
        i += 1
        continue
    time = 0
    if a == i:
        print("%d"%a)
        break
    ab = a
    while a % i == 0:
        a = a / i
        time += 1
    if time != 1:
        if(ab == math.pow(i,time)):
            print("%d^%d" % (i, time))
        else:
            print("%d^%d" % (i, time), end=" * ")
    else:
        print(i, end=" * ")
    i += 1
