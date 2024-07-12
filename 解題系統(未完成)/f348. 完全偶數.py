num = str(input())
change = []
for i in range(len(num)):
    if int(num[i]) % 2 == 1: change.append(1)
    else: change.append(0)
print(change)