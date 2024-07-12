n = int(input())
a = input()
list = list(map(int,a.split()))
right_min = [0]*n
right_min[-1]  = list[-1]

for i in range(n-2, -1, -1):
    right_min[i] = min(list[i],right_min[i+1])

ans = []
for i in range(len(list)):
    ans_ele = list[i] - right_min[i]
    ans.append(ans_ele)
print(max(ans))
