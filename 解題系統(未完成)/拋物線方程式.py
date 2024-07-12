while 1:
    try:
        read = []
        read.extend(input().split())
        a,b,c,d = int(read[0]),int(read[1]),int(read[2]),int(read[3])
        son = d-b
        mon = c-a
        double_mon = mon**2
        for i in range(1,abs(c-a)+1):
            if son % i == 0 and double_mon % i == 0 and i > 1:
                son /= i
                mon /= i
                double_mon /= i
                if i > son or i > double_mon:
                    break
        _y = int(double_mon)
        _x2 = int(son)
        _x = int(son * -2 * a)
        _c = int(a**2 *son +b*double_mon)
        print(f"{_y}y = {_x2}x^2 + {_x}x + {_c}")
    except:
        break