n = int(input())
time = 0
for i in range(2,10):
    if n % i == 0:
        if len(str(n//i)) == 9: time += 1
if time == 0: print("yes")
else: print("no")