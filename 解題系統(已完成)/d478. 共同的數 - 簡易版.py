from collections import Counter

n, m = map(int,input().split())
for i in range(n):
    a = input()
    num_1 = list(map(int,a.split()))
    b = input()
    num_2 = list(map(int,b.split()))
    num = num_1 + num_2
    count = Counter(num)
    result = [num for num, i in count.items() if i == 2]
    print(len(result))

