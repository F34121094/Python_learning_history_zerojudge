while 1:
    try:
        a,b,c,d,e = map(str,input().split())
        a,b,c,d = int(a),int(b),int(c),int(d)
        if e == "+":
            mother = b * d
            son = a * d + b * c


    except:
        break