a,b= map(int,input().split())
if a > b:
    temp = a
    a = b
    b = temp

if a % 2 == 0:first = a
else: first = a+1
if b % 2 == 0: last = b
else : last = b-1

n = (last-first)//2 +1
sum = (first+last)//2 * n
print(sum)