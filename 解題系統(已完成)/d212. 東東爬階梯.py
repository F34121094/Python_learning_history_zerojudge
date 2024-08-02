#咚咚一次走1階或2階

def walk(n):
    if n <= 2:
        return n
    #應該要使用動態規劃
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2

    for i in range(2,n):
        dp[i] = dp[i-1]+ dp[i-2]
    return dp[n-1]

while 1:
    try:
        n = int(input())
        ans = walk(n)
        print(ans)
    except:
        break