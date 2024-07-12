n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    #a為 a*a的一個矩陣  b = 1順 b = 2逆
    max = a*a
    arr= []
    for j in range(a):
        arr.append([0 for _ in range(a)])
    x,y = 0,0
    max_x ,max_y = a-1,a-1
    start_x ,start_y = 0,0
    turn = 1 #轉向

    for j in range(1,max+1):
        if b == 1: arr[y][x] = j
        else: arr[x][y] = j

        if i == max: break

        if turn == 1: x = x + 1 #右
        if turn == 2: y = y + 1 #下
        if turn == 3: x = x - 1 #左
        if turn == 4: y = y - 1 #上



        if turn == 1 and y == start_y and x == max_x:
            turn = 2
            start_y += 1
        if turn == 2 and x == max_x and y == max_y:
            turn = 3
            max_x -= 1
        if turn == 3 and y == max_y and x == start_x:
            turn = 4
            max_y -= 1
        if turn == 4 and x == start_x and y == start_y:
            turn = 1
            start_x += 1

    for x in arr:
        for j in x:
            print(f"{j:5d}",end = '')
        print()
