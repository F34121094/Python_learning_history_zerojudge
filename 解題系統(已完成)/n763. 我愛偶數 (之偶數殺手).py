from collections import deque
n = int(input())
i = input()
list_num = deque(map(int,i.split()))

while len(list_num) != 1:
    now = list_num.popleft()
    if now % 2 == 0:
        list_num.popleft()
    list_num.append(now)

print(*list_num)
