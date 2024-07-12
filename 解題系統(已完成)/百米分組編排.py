n = int(input())
group = int(n / 8)
dic = {}
for i in range(n):
    key, value = input().split()
    dic[key] = float(value)
#把字典裡的數字填入
rank = []
for i in range(n):
    a = min(dic,key = dic.get)
    rank.append(a)
    dic.pop(a)
#rank為名次
final = []
for i in range(group):
    final.append([])

time = 0
dire = 0
for i in range(len(rank)):
    time += 1
    if dire == 0:   #順
        a = i % group
        final[a].append(rank[i])

    if dire == 1:   #逆
        a = (group - 1) - (i % group)
        final[a].append(rank[i])
    if time % group == 0:
        dire = 1 - dire

for i in range(group):
    print(f"{i+1} {final[i][6]} {final[i][4]} {final[i][2]} {final[i][0]} {final[i][1]} {final[i][3]} {final[i][5]} {final[i][7]}")