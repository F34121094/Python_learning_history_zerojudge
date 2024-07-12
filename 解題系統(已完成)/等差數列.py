a,b,c = map(int,input().split())
if c > 0:
    for i in range(a,b+1,c):
        print(i,end = " ")
elif c < 0:
    for i in range(a,b-1,c):
        print(i,end = " ")