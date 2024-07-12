while 1:
    try:
        a,b,c,d, key = input().split()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        #先通分
        if key == "+" :
            if b != d:
                a *= d
                c *= b
                b *= d
            result = a + c
            if result >= b : large = result
            else : large = b
            for i in range(2,int(large**0.5) + 1):
                if b == 1: break
                if result % i == 0 and b % i == 0:
                    result = result // i
                    b = b // i
            if result == b:
                result = 1
                b = 1
            if b == 1: print(result)
            else:
                if b < 0 :
                    b = -b
                    result = -result
                print(f"{result}/{b}")
        elif key == "-" :
            if b != d:
                a *= d
                c *= b
                b *= d
            result = a - c
            if result >= b : large = result
            else : large = b
            for i in range(2, int(large ** 0.5) + 1):
                if b == 1: break
                if result % i == 0 and b % i == 0:
                    result = result // i
                    b = b // i
            if result == b:
                result = 1
                b = 1
            if b == 1:
                print(result)
            else:
                if b < 0:
                    b = -b
                    result = -result
                print(f"{result}/{b}")

        elif key == "*":
            result = a * c
            b *= d
            if result == b:
                result = 1
                b = 1
            if result >= b : large = result
            else : large = b
            for i in range(2, int(large ** 0.5) + 1):
                if b == 1: break
                if result % i == 0 and b % i == 0:
                    result = result // i
                    b = b // i
            if b == 1:
                print(result)
            else:
                print(f"{result}/{b}")
        else :
            result = a * d
            b *= c
            if result == b:
                result = 1
                b = 1
            if result >= b : large = result
            else : large = b
            for i in range(2, int(large ** 0.5) + 1):
                if b == 1: break
                if result % i == 0 and b % i == 0:
                    result = result // i
                    b = b // i
            if b == 1:
                print(result)
            else:
                print(f"{result}/{b}")
    except:
        break