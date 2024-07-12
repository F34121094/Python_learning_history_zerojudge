n = int(input())

str = input().split()

time = int(input())
for _ in range(time):
    a = str.pop(0)
    str.append(a)
print(*str)