from collections import Counter

a = input()
num = list(map(int,a.split()))
counter = Counter(num)
result = [num for num, count in counter.items() if count == 2]
print(*result)
