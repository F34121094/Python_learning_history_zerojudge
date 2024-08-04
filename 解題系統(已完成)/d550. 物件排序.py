n,m = map(int,input().split())
dp = []
for i in range(n):
    num = list(map(int,input().split()))
    dp.append(num)
dp.sort()
for i in dp:
    print(*i)