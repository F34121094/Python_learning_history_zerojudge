n ,t = map(int,input().split())
list = []
for i in range(n):
    a,b = map(int,input().split())
    list.append([a,b])
total = 0

while t:
    list.sort(reverse = True)
    now = list[0][0]
    total += now
    list[0][0] = list[0][0] - list[0][1]
    t -= 1

print(total)