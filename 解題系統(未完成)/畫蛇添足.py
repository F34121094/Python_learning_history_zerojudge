while 1:
    try:
        n, m = map(int,input().split()) #v
        if n == "" or m == "":
            continue
        #接下來有 m 行
        farm = []   #farm大小為 (n+2) * (n+2)
        farm.append(["-" for i in range(n+2)])
        for i in range(n):
            farm.append([" " for i in range(n+2)])
            farm[i + 1][0] = "|"
            farm[i + 1][n + 1] = "|"
        farm.append(["-" for i in range(n + 2)])

        # farm 建構完成
        maze = []
        for i in range(m):
            x,y = map(int,input().split())
            maze.append([x,y])
        # maze 接收完成
        while len(maze) != 1:
            start = maze.pop()
            next = maze.pop()
            if start[0] == next[0]:
                while start != next:
                    farm[start[0]][start[1]] = "*"
                    if start[1] > next[1]: start[1] -= 1
                    else: start[1] += 1
            if start[1] == next[1]:
                while start != next:
                    farm[start[0]][start[1]] = "*"
                    if start[0] > next[0]: start[0] -= 1
                    else: start[0] += 1
            maze.append(next)
        for i in range(len(farm)):
            output = "".join(farm[i])
            print(output)
    except:
        break