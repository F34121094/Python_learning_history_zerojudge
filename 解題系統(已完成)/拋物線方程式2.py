while 1:
    try:
        read = []
        read.extend(input().split())
        a,b,c,d = int(read[0]),int(read[1]),int(read[2]),int(read[3])
        son = d-b
        double_mon = (c-a)**2
        #錯誤應該在for迴圈裡
        for i in range(1,abs(c-a)+1):
            if son % i == 0 and double_mon % i == 0 and i > 1:
                while 1:        #因為可能會遇到分母分子可以被 i 整除很多次的情況所以要確保他已經被 i 除到不能再除了
                    son /= i
                    double_mon /= i
                    if son % i != 0 or double_mon % i != 0:
                        break
                if i > abs(son) or i > double_mon: #這裡應該沒有錯
                    break
        #這以下不會有錯
        _y = int(double_mon)
        _x2 = int(son)
        _x = int(son * -2 * a)
        _c = int(a**2 *son +b*double_mon)
        print(f"{_y}y = {_x2}x^2 + {_x}x + {_c}")
    except:
        break