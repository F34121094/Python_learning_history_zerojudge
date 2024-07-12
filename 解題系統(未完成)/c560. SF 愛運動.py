def solve(a,b):
    gap = b - a
    if gap <= 2:
        return 1
    dp = [0] * (gap + 1)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4,gap+1):
        dp[i] = dp[i-3] + dp[i-1]

    return dp[gap]


n , m = map(int,input().split())

a = input()
station = list(map(int,a.split()))
station.insert(0,0)
station.append(n)

ans_list = []
for i in range(len(station)-1):
    ans = solve(station[i],station[i+1])
    ans_list.append(ans)
result = 1
for i in ans_list:
    result *= i
print(result)
#一定會走到每一個休息站