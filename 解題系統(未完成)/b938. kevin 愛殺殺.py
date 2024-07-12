n, m = map(int,input().split())
#n,m
num = [i for i in range(n)]
be_killed = list(map(int, input().split()))
#m 個數字 k1'k2'k3...km
#殺掉
for i in be_killed:
    i = int(i)
    if i == n :
        print("0u0 ...... ?")
        continue
    if num[i-1] == 0:
        print("0u0 ...... ?")
        continue
    time = 0
    while num[i] == 0:
        i += 1
        if i == n:
            print("0u0 ...... ?")
            time += 1
            break

    if time == 0:
        print(num[i])
        num[i] = 0


