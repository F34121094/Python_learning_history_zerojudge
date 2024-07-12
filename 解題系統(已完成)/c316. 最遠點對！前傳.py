n = int(input())
list = []
distance = []
for i in range(n):
    a,b = map(int,input().split())
    list.append([a,b])
    if i == n-1: break
    distance.append([])
k = 0
while list:
    point = list.pop(0)
    for i in range(len(list)):
        point_2 = list[i]
        distance[k].append(((point[0]-point_2[0])**2 + (point[1]-point_2[1])**2) ** 0.5)
    k += 1
max_value = max(max(i) for i in distance)
for i in range(len(distance)):
    for j in range(len(distance[i])):
        if distance[i][j] == max_value:
            print(f"{i} {j+i+1}")
            break