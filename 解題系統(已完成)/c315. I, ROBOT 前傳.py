n = int(input())
list = []
for i in range(n):
    a,b = map(int,input().split())
    list.append([a,b])
position = [0,0]
while list:
    step = list.pop()
    if step[0] == 0:
        position[1] += step[1]
    elif step[0] == 1:
        position[0] += step[1]
    elif step[0] == 2:
        position[1] -= step[1]
    else:
        position[0] -= step[1]
print(*position)
