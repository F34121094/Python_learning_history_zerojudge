n= int(input())
for abc in range(n):
    x,a,b = map(int,input().rstrip().split())
    if b > a :
        temp = b
        b = a
        a = temp
    #a一定較大
    if x % a == 0:
        print(x//a)
        continue
    div_a = x // a
    last = x % a
    record_b = 0
    for i in range(div_a + 1):
        record_a = div_a - i
        if last % b == 0:
            record_b = last // b
            break
        last += a
    if record_b == 0:
        print("-1")
    else:
        print(record_a + record_b)
