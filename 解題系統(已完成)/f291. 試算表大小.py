dic = {
    "A":1,"B":2,"C":3,"D":4,"E":5,
    "F":6,"G":7,"H":8,"I":9,"J":10,
    "K":11,"L":12,"M":13,"N":14,"O":15,
    "P":16,"Q":17,"R":18,"S":19,"T":20,
    "U":21,"V":22,"W":23,"X":24,"Y":25,
    "Z":26
}
str = input()
str_list = []
str_number = []
for i in range(len(str)):
    if str[i] in dic:
        str_list.append(dic.get(str[i]))
    else:
        str_number.append(str[i])
str_value = int("".join(str_number))
str_total = 0
str_i = 1

while str_list:
    str_total += str_i * str_list.pop()
    str_i *= 26
print(str_total * str_value)
