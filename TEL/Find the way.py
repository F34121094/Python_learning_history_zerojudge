while 1:
    try:
        a,b = map(int,input().split())
        sum_a = 1
        sum_b = 1
        for i in range(a,a-b,-1):
            sum_a *= i
        for i in range(2,b+1):
            sum_b *= i
        print(len(str(sum_a//sum_b)))
    except:
        break