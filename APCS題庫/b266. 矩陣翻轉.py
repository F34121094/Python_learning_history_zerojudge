r,c,m = map(int,input().split())
list_num = []
for i in range(r):
    a = input()
    a = list(map(int,a.split()))
    list_num.append(a)
operation = input()
operation = list(map(int,operation.split()))

for i in operation:
    if i == 1:
        for j in range(len(list_num)//2):
            temp = list_num[-(j+1)]
            list_num[-(j + 1)] = list_num[j]
            list_num[j] = temp
    else:
        #用r,c的關係來做
        new_list = [[] for i in range(c)]
        for j in range(c):
            for k in range(r-1,-1,-1):
                new_list[j].append(list_num[k][j])
        list_num = new_list
        t = r
        r = c
        c = t
print(f"{r} {c}")
for i in range(r):
    print(*list_num[i])

