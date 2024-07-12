import sys

while 1:
    try:
        a = input()
        if a == "0": break
        total = 0
        for i in range(len(a)):
            a[i].upper()
            if ord(a[i]) > 96 or ord(a[i]) < 65:
                print("Fail")
            num = ord(a[i]) - 64
            total += num

        print(total)
    except:
        break