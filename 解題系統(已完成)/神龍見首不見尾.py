num = input()
print(num)
for i in range(len(num)-1,0,-1):
    for j in range(i):
        print(num[j],end = "")
    print()


