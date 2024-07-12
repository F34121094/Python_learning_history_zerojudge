def solve(n):
    years = n - 1
    y = years % 12
    if y < 0: y += 12
    if y == 0: print("鼠")
    elif y == 1: print("牛")
    elif y == 2:
        print("虎")
    elif y == 3:
        print("兔")
    elif y == 4:
        print("龍")
    elif y == 5:
        print("蛇")
    elif y == 6:
        print("馬")
    elif y == 7:
        print("羊")
    elif y == 8:
        print("猴")
    elif y == 9:
        print("雞")
    elif y == 10:
        print("狗")
    elif y == 11:
        print("豬")

while 1:
    try:
        n = int(input())
        solve(n)
    except:
        break