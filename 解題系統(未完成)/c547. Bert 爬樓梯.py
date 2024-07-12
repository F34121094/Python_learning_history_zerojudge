def solve(n):
    if n <= 2:
        return n

    prev2 , prev1 =1 ,2

    for i in range(3,n+1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return curr
while 1:
    try:
        n = int(input())
        if n < 0 :
            print(0)
            continue
        elif n <= 2:
            print(n)
            continue
        ans = solve(n)
        print(ans)
    except:
        break