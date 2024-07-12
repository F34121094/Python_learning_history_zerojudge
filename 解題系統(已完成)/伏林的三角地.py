a,b,c = map(int,input().split())
s = (a+b+c)/2
A = int(s*(s-a)*(s-b)*(s-c))
print(A)