while 1:
    try:
        n = int(input())
        if n % 2 == 1:
            print(n-1)
        else:
            print(n)
    except:
        break