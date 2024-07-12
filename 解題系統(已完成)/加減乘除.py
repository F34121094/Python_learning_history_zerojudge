a,b,c = input().split()
ans = 0
a = int(a)
c = int(c)
if b =="+": ans+= a+c
elif b =="-": ans += a-c
elif b =="*": ans += a*c
elif b == "/": ans += a//c
print(ans)