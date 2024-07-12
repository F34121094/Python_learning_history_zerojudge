a,b = map(int,input().split())
if b < a:
    b += 100
gap = b-a
print(gap)