read = int(input())
for i in range(read):
    x,y = map(int,input().split())
    yee = 100 - int(x+y)
    if yee >0 and yee <=30:print("sad!")
    elif yee>30 and yee<=60:print("hmm~~")
    elif yee>60 and yee<100:print("Happyyummy")
    else:print("evil!!")