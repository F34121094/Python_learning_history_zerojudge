dic = {
    "A":1,"B":2,"C":3,"D":4,"E":5,
    "F":6,"G":7,"H":8,"I":9,"J":10,
    "K":11,"L":12,"M":13,"N":14,"O":15,
    "P":16,"Q":17,"R":18,"S":19,"T":20,
    "U":21,"V":22,"W":23,"X":24,"Y":25,
    "Z":26
}
a,b = input().split()
a_list = []
b_list = []
for i in range(len(a)):
    a_list.append(dic.get(a[i]))
for i in range(len(b)):
    b_list.append(dic.get(b[i]))
a_total = 0
b_total = 0
a_i = 1
b_i = 1
while a_list:
    a_total += a_i * a_list.pop()
    a_i *= 26
while b_list:
    b_total += b_i * b_list.pop()
    b_i *= 26
print(b_total - a_total + 1)