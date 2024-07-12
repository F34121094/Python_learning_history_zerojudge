read = input().split()
for i in range(1,len(read)-1):
    print(read[i],end = " ")
    print(read[0],end = " ")
print(read[len(read)-1])