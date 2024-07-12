while 1:
    n,m = map(int,input().split())
    if n == 0 and m == 0: break
    vocabulary = []
    for i in range(n):
        a = input().strip()
        vocabulary.append(a)
    a = input()
    num = list(map(int,a.split()))
    vo_new = "".join(vocabulary)
    result = ''.join(vo_new[num[i] - 1] for i in range(m))
    print(result)
