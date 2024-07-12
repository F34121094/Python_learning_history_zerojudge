arr = []
while 1 :
    try:
        read = input()
        if read in arr:
            print("YES")
        else:
            print("NO")
            arr.append(read)
    except:
        break