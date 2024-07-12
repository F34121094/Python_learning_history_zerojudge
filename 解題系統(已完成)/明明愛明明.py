from sys import stdin

for read in stdin:
    str = read.lower()
    ok = lambda a : ord(a) >=97 and ord(a)<=122
    str = "".join(filter(ok,str))
    # print(str)
    time = 0
    for i in range(97,123):
        if str.count(chr(i)) % 2 == 1:
            time += 1
            if(time == 2):
                print("no...")
                break
    if time <= 1:
        print("yes !")


