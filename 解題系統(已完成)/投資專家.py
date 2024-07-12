#input 本金 現價
#若虧損 >= 10 % dispose

n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    x = 100 * ((b-a)/a)
    if x == 0:
        print("0.00%",end = " ")
    elif x < 0:
        print("{:.2f}%".format(x-0.00001),end = " ")
    elif x > 0:
        print("{:.2f}%".format(x+0.00001),end = " ")
    if(x <= -7 or x >= 10):
        print("dispose")
    else:
        print("keep")