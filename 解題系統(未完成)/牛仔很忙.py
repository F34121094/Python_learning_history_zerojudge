x,y = map(int,input().split())
h = x + 2
m = y + 30
if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

H = str(h)
M = str(m)
if len(H) == 1 : H = "0"+H
if len(M) == 1 : M = "0"+M
print(f"{H}:{M}")