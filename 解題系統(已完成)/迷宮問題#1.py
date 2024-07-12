def bfs(start,end,maze):
    path = []
    path.append(start)
    queue = []
    queue.append(start)
    time = 1
    rank_node = 1
    while len(queue) > 0 :
        y,x = queue.pop(0)

        for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
            next_x,next_y = x+dx , y+dy
            if [next_y,next_x] == end:
                print(time+1)
                return
            if maze[next_y][next_x] != "#" and [next_y,next_x] not in path:
                path.append([next_y,next_x])
                queue.append([next_y,next_x])

        rank_node -= 1
        if rank_node == 0:
            rank_node = len(queue)
            time += 1
    print("No solution!")


n = int(input())
maze = []
for _ in range(n):
    maze.append(input())

start = [1,1]
end = [n-2,n-2]
bfs(start,end,maze)
