n = int(input())
for j in range(n):
    a,b,c,d = input().split()
    a,b,c,d=int(a),int(b),int(c),int(d)
    if(d - c == c - b):
        e = d + (d - c)
    else:
        e = d * (d / c)
    e =int(e)
    print(a,b,c,d,e)