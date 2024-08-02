def solve(n,current):
    if n == 0:
        return current
    else:
        return solve(n-1,current+[0]) + solve(n-1,current+[1])
while 1:
    try:
        current = []
        n = int(input())
        ans = solve(n,current)
        for i in range(len(ans)):
            print(ans[i],end = '')
            if (i+1) % n == 0:
                print()

    except:
        break