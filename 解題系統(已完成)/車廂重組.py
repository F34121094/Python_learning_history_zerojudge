arr = []

while 1:
   try:
      arr.extend(list(map(int, input().split())))
   except:
      break
n = arr.pop(0)
time = 0

for i in range(n-1,0,-1):
    for j in range(i):
        if (arr[j] > arr[j+1]):
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

            time += 1

print(time)
