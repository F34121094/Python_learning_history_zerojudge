n = int(input())
family = [[] for i in range(n)]
parent = []
for i in range(n-1):
    a,b = map(int,input().split())
    family[a].append(b)
    if a not in parent:
        parent.append(a)
for i in parent:
    time = 0
    for j in range(len(family)):
        if i in family[j]:
            time += 1
    if time == 0: old = i
while 1:
    #定義一個已經經過的+一個stack
    #定義目前經過的最長距離
    seen = []
    stack = []
    seen.append(family[7])
    stack.append(family[7])
    while stack:
        now = stack.pop()
        stack.append(family[now])


