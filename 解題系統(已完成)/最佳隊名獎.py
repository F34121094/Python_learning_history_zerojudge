str = list(map(ord,input()))
print(str[0],end = "")
for i in range(1,len(str)):
    print("_",end = "")
    print(str[i],end = "")