#紅羅波(1) = + xg
#白羅波(2) = + yg
#黃羅波(3) = - zg
#黑羅波(4) = - wg (中毒 - ng/day)
#先被毒，再補血
#兔子 mg
n = int(input())
for i in range(n):
    set = list(map(int,input().split()))
    #set[0]=紅 set[1]=白,,,set[4]=體重
    eat = list(map(str,input().split()))
    weight = set[5]
    poison = 0
    for day in range(len(eat)):
        weight -= set[4]*poison
        if weight <= 0:
            print("bye~Rabbit")
            break
        if eat[day] == "1":
            weight += set[0]
        elif eat[day] == '2':
            weight += set[1]
        elif eat[day] == '3':
            weight -= set[2]
            if weight <= 0:
                print("bye~Rabbit")
                break
        elif eat[day] == '0':
            weight = weight
        else:
            weight -= set[3]
            if weight <= 0:
                print("bye~Rabbit")
                break
            poison += 1
    if weight > 0 :
        print(weight,end ="")
        print("g")
