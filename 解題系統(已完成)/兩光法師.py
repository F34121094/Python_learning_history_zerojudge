mon,day = map(int,input().split())
s = (mon*2+day)%3
if s==0:
    print("普通")
elif s==1:
    print("吉")
else:
    print("大吉")