a,b = map(int,input().split())
time = 0
if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    for i in range(a,b+1,4):
        if (i%4 == 0 and i%100 != 0) or i%400 == 0:
            time += 1
else:
    while 1:
        a += 1
        if (a%4 == 0 and a%100 != 0) or a%400 == 0: break
    for i in range(a, b+1, 4):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            time += 1
print(time)