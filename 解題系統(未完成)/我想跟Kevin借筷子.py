while 1:
    try:
        read = int(input())
        time = 0
        while read > 0:
            if read % 2 == 0:
                read -= read/2
                time += 1
            else:
                read -= (read+1)/2
                time += 1
        print(time)
    except:
        break