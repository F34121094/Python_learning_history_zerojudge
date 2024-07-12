id = int(input())
time = 0
for i in range(2,10000):
    if i == id: continue
    if id % i == 0: time+=1
if time == 0: print("yes")
else:print("no")