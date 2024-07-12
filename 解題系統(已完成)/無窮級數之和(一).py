from math import log
def cal(n):
    if n == 1: return 1
    else: return 1/n + cal(n-1)
while 1:
    try:
        num = int(input())
        if num <= 100: ans = cal(num)
        else: ans = log(num) + 0.577215664901532860606512090082402431042159335

        print(f"{ans:.3f}")
    except:
        break