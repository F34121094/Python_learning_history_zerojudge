n = int(input())
arr = input().split()
for i in range(len(arr)):
    arr[i] = int(arr[i])
print(max(arr))