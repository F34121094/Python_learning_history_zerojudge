import sys

n = int(input())
white = []
black = []
i = input()
list = list(map(int,i.split()))
while list:
    a = list.pop()
    if a > 0:white.append(a)
    else: black.append(a)
if len(white) == 0:
    print("0")
    sys.exit()
if len(black) == 0:
    print("0")
    sys.exit()
white.sort(reverse = True)
black.sort()
result = []
while 1:
    w_m = white.pop()
    b_m = black.pop()
    if w_m > -(b_m):
        result.append("-")
        white.append(w_m)
    else:
        result.append("+")
        black.append(b_m)

    if len(white) == 0:
        result.append("-")
        break
    elif len(black) == 0:
        result.append("+")
        break
set = 0
while len(result) != 1:
    a = result.pop()
    if a != result[len(result) - 1]:
        set += 1
print(set)

