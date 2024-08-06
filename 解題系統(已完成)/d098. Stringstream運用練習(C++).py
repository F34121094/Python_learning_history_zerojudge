while 1:
    try:
        input_list = list(map(str,input().split()))
        total = 0
        for i in input_list:
            if i.isdigit():
                total += int(i)

        print(total)
    except:
        break