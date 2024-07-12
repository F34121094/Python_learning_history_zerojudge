n = int(input())
line = []
for i in range(n):
    a, b = map(int, input().split())
    line.append([a, b])
line.sort(key=lambda a: a[1])
_max = line[n - 1][1]
length = [0 for i in range(_max)]
print(length)
for i in range(n):

while (line[i][0] - 1) != line[i][1]:
    length[line[i][0] - 1] = 1
    line[i][0] += 1
print(length)
