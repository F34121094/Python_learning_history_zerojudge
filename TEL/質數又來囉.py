def cal(num):
    for i in range(5 ,int(num**0.5)+1 ,6):
        if num % i == 0: return False
        elif num % (i+2) == 0 : return False
    return True

while 1:
    try:
        a, b = map(int,input().split())
        time = 0
        for i in range(a,b+1):
            if i <= 1 or i % 2 == 0 or i % 3 == 0: continue
            if cal(i):
                time += 1
        print(time)
    except:
        break