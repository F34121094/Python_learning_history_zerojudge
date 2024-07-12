a,b,c = map(int,input().split())
if a>c:
    temp = c
    c = a
    a = temp
if b>c:
    temp = c
    c = b
    b = temp
if c*c == a*a + b*b: print("right triangle")
elif (c*c < a*a + b*b): print("acute triangle")
else:print("obtuse triangle")
