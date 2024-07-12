read = input().split()
for i in range(len(read)):
    if i == len(read)-1 : print(f"{read[i]} little Indians")
    else:print(f"{read[i]} little,",end =" ")