from sys import stdin
import itertools

for read in stdin:
    n = int(read)
    arr = [str(i) for i in range(1,n+1)]
    arr = arr[::-1]
    ans = itertools.permutations(arr)
    for i in ans:
        print("".join(i))