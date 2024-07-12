#先做一個轉換數字的程式
dic = {"I":1,
       "V":5,
       "X":10,
       "L":50,
       "C":100,
       "D":500,
       "M":1000}
keys = ["I","V","X","L","C","D","M"]
def str_to_number(str):
    total = 0
    arr = []
    for i in range(len(str)):
        arr.append(dic[str[i]])
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            total += arr[i]
        else:
            total -= arr[i]
    total += arr[len(arr)-1]
    return total
def number_to_str(num):
    while num >= 1000:
        num -= 1000
        print("M",end = "")
    while num >= 900:
        num -= 900
        print("CM",end = "")
    while num >= 500:
        num -= 500
        print("D",end = "")
    while num >= 400:
        num -= 400
        print("CD",end = "")
    while num >= 100:
        num -= 100
        print("C",end = "")
    while num >= 90:
        num -= 90
        print("XC",end = "")
    while num >= 50:
        num -= 50
        print("L",end = "")
    while num >= 40:
        num -= 40
        print("XL",end = "")
    while num >= 10:
        num -= 10
        print("X",end = "")
    while num >= 9:
        num -= 9
        print("IX",end = "")
    while num >= 5:
        num -= 5
        print("V",end = "")
    while num >= 4:
        num -= 4
        print("IV",end = "")
    while num > 0:
        num -= 1
        print("I",end = "")

#main
while 1:
    ipt = input()
    if ipt == "#":
        break
    a,b = map(str,ipt.split())
    gap =abs(str_to_number(a) - str_to_number(b))
    if gap == 0:
        print("ZERO")
    else:
        number_to_str(gap)
        print()