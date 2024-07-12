while 1:
    try:
        vote = input().split()
        can = ["A","B","C"]
        #所有第三名的支持者都會把票投給第二名
        for i in range(3):
            vote[i] = int(vote[i])
        a = max(vote)
        b = min(vote)
        max_in = vote.index(a)
        min_in = vote.index(b)
        for i in range(3):
            if i != max_in and i != min_in:
                vote[i] += b
                if vote[i] > a:print(can[i])
                else: print(can[max_in])

    except:
        break