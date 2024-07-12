time = 0
for _ in range(5):
    a,b,c = map(int,input().split())
    if a+b>c:
        if a+c>b:
            if b+c>a: time +=1
print(time)