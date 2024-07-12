n= int(input())
a = "_"
b = "*"
for i in range(1,n+1):
    print(f"{a*(n-i)}{b*i}",end = "")
    print(f"{b*(i-1)}{a*(n-i)}")