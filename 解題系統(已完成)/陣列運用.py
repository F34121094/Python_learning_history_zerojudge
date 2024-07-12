while True:
    try:
        a,b,c = map(int,input().rstrip().split())
        ans = a*(10**c) // b
        st_ans = str(ans)
        if len(st_ans) < c:
            for i in range(c-len(st_ans)):
                st_ans = "0" + st_ans
        m = st_ans[(c*-1):]
        n = st_ans[:(c*-1)]
        if n == "":
            n = "0"
        print(f"{n}.{m}")
    except:
        break