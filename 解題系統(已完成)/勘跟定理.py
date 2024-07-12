a , b, c , d, e, f =map(int,input().split())
time = 0
if a == 0 and b == 0 and c == 0 and d == 0 and e == 0 and f == 0:
    print("Too many... = =\"")
    time += 1
else:
    for i in range(-36,37):
        j = i+1
        if (a*i**5 + b*i**4 + c*i**3 + d*i**2 + e*i + f) == 0:
            print(f"{i} {i}")
            time += 1
        elif (a*i**5 + b*i**4 + c*i**3 + d*i**2 + e*i + f) < 0 < (a*j**5 + b*j**4 + c*j**3 + d*j**2 + e*j + f):
            print(f"{i} {j}")
            time += 1
        elif (a*i**5 + b*i**4 + c*i**3 + d*i**2 + e*i + f) > 0 > (a*j**5 + b*j**4 + c*j**3 + d*j**2 + e*j + f):
            print(f"{i} {j}")
            time += 1
if time == 0: print("N0THING! >\\\\\\<")