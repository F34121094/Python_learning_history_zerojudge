import math
a,b,c = map(int,input().split())
ans = b**2 - 4*a*c
if(ans > 0):
    print("Two different roots",end = " ")
    x1 = (-b + math.sqrt(ans)) / (2 * a)
    x2 = (-b - math.sqrt(ans)) / (2 * a)
    if(x1 < x2):
        temp = x1
        x1 = x2
        x2 = temp
    print("x1=%d , x2=%d"%(x1,x2))
elif(ans==0):
    if(a == 0):
        x1 = c/b
    else:
        print("Two same roots",end=" ")
        x1 = (-b + math.sqrt(ans)) / (2 * a)
    print("x=%d"%x1)
else:
    print("No real root")
