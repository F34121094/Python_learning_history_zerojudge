def solve(n):
    years = n - 1906
    a = years % 10
    b = years % 12
    if a < 0: a += 10
    elif b < 0: b+= 12
    if a == 0: print("丙",end = '')
    elif a == 1: print("丁", end = '')
    elif a == 2: print("戊",end = '')
    elif a == 3: print("己", end = '')
    elif a == 4: print("庚", end= '')
    elif a == 5: print("辛", end = '')
    elif a == 6: print("壬",end = '')
    elif a == 7: print("癸", end = '')
    elif a == 8: print("甲", end = '')
    else: print("乙", end = '')

    if b == 0: print("午")
    elif b == 1: print("未")
    elif b == 2: print("申")
    elif b == 3: print("酉")
    elif b == 4: print("戌")
    elif b == 5: print("亥")
    elif b == 6: print("子")
    elif b == 7: print("丑")
    elif b == 8: print("寅")
    elif b == 9: print("卯")
    elif b == 10: print("辰")
    else: print("巳")
while 1:
    try:
        n = int(input())
        solve(n)
    except:
        break