read = input()
length = len(read)
for i in range(length):
    if i == 0 or i == length-1:print(read[i],end = "")
    else:print("_",end = "")