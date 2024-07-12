h, m = map(int,input().split())
if 17 >= h >= 7:
    if h == 17:
        if m >= 0: print("Off School")
        else:print("At School")
    elif h == 7:
        if m < 30 : print("Off School")
        else:print("At School")
    else: print("At School")
else:print("Off School")
