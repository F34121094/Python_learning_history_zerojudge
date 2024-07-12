h,m,s = map(int,input().split())
if s >= 60:
    m += s//60
    s %= 60
if m >= 60:
    h += m//60
    m %= 60
if h >= 24: h %= 24
h = str(h)
m = str(m)
s = str(s)
if len(h) == 1: h = "0"+h
if len(m) == 1: m = "0"+m
if len(s) == 1: s = "0"+s
print(f"{h}:{m}:{s}")