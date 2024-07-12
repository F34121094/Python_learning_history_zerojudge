#捕獲+3 傳送、進化 +1
c,w = map(int,input().split())
ans = 0
while w > 0:
    if c >= 12:
        c -= 11
        ans += 1
    else:
        w -= 1
        c += 1
print(ans)