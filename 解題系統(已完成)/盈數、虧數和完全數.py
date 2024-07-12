while 1:
    try:
        n = int(input())
        total = 0
        for i in range(2,n):
            if n % i == 0:
                total += i
        total += 1
        if total == n:print("完全數")
        elif total > n : print("盈數")
        else:print("虧數")
    except:
        break