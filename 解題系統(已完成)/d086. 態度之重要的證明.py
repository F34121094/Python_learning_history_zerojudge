while 1:
    try:
        n = input()
        if n == "0": break
        n_low = n.lower()
        total = 0
        TF = True
        for i in range(len(n_low)):

            num = (ord(n_low[i]) - 96)
            if num < 1 or num > 26:
                TF = False
                break
            total += num
        if (TF): print(total)
        else: print("Fail")

    except:
        break