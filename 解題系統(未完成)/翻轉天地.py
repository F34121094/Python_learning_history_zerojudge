n = int(input())

for i in range(n):
    a,b = map(int , input().split())
    arr = []
    for j in range(a):
        arr.append(input().split()) #成功存入
    #驗證
    x1,y1 = 0,0
    x2,y2 = b - 1, a - 1

    time = int((a*b)/2)
    turn = 1
    ys = 1
    for i in range(time):
        if arr[y1][x1] == arr[y2][x2]:
            x1 += 1
            x2 -= 1
            turn += 1
            if turn == b:
                turn = 1
                y1 += 1
                y2 -= 1
                x1 = 0
                x2 = b-1
                continue
            else: continue
        else:
            ys -= 1
            break

    if ys == 0: print("keep defending")
    else: print("go forward")
