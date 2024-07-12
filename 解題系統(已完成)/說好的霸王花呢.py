while 1:
    try:

        n,m = map(int,input().split())
        #共有n個花瓣，第一次拔一個，後面每一次都多拔m個
        last = n-1
        if m == 0 :
            print("Go Kevin!!")
        else:
            if last % m == 0: print("Go Kevin!!")
            else: print("No Stop!!")
    except:
        break