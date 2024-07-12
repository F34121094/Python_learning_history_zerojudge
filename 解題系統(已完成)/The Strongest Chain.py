n= int(input())
a= []
for i in range(n):
    b = input().split()
    b.pop(0)
    for j in range(len(b)):
        b[j] = int(b[j])
    a.append(b)
c = []
for i in range(n):
    c.append(min(a[i]))
print(max(c))