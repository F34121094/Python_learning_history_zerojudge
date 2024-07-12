str = input().split()
a = []
b = []
c = []
for i in range(len(str)):
    if i % 3 == 0: a.append(str[i])
    elif i % 3 == 1: b. append(str[i])
    else : c.append(str[i])
print(*a)
print(*b)
print(*c)