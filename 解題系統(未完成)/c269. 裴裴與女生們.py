while 1:
    try:
        str = input()
        n, T = map(int,input().split())
        weight = []
        value = []
        type = []
        for i in range(n):
            a,b,c = map(int,input().split())
            weight.append(a)
            value.append(b)
            type.append(c)
        dp = [[0] * (T) for _ in range(n + 1)]

        for i in range(1,n+1):
            for w in range(T+1):
                if weight[i-1] <= w:
                    dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i-1]] + value[i-1])
                else:
                    dp[i][w] = dp[i-1][w]

    except:
        break