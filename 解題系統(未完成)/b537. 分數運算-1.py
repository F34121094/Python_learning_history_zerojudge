def solve(value):
    if value == 1:
        return 1
    if value > 1:
        return
    if value < 1:

        
while 1:
    try:
        a,b = map(int,input().split())
        value = a/b
        solve(value)
    except:
        break
