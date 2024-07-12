def a(n):
    def b(s = '',l = 0,r = 0):
        if len(s) == n*2 :
            ans.append(s)
            return

        if l < n: b(s + '(', l + 1 , r)
        if r < l: b(s + ')', l , r + 1)

    ans = []
    b()
    return ans

while 1:
    try:
        n = int(input())
        for i in a(n):
            print(i)
    except:
        break