n = int(input())
num = input().split()
time = 0
for i in num:
    if int(i) <= 10: time += 1
print(time)