while 1:
    try:
        a = input()
        num = list(map(int,a.split()))
        total = 0
        for i in range(len(num)):
            total += num[i]
        print(total)
    except:
        break