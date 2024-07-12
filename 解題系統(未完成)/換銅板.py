n = int(input())
type = input().split()
for i in range(len(type)):
    type[i] = int(type[i])
sum = int(input())
stack = []
result = []
for i in range(n-1,-1,-1):
    if sum >= type[i]:
        a = sum // type[i]
        sum %= type[i]
        stack.append(a)
        stack.reverse()
result.append(stack)
for i in range(1,n):
    if stack[i] != 0:
print(result)