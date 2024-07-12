while True:
    try:
        a = int(input())
        total = 0
        for i in range(2,a):
            while a % i == 0:
                a /= i
                total += i
            if a == 1: break
            if total == 0 and i > int((a**0.5)+0.00001): break
        if total == 0: print(a)
        else: print(total)
    except:
        break