dic = {"A":"10","B":"11","C":"12","D":"13",
       "E":"14","F":"15","G":"16","H":"17",
       "I":"34","J":"18","K":"19","L":"20",
       "M":"21","N":"22","O":"35","P":"23",
       "Q":"24","R":"25","S":"26","T":"27",
       "U":"28","V":"29","W":"32","X":"30",
       "Y":"31","Z":"33"}

muti = [8,7,6,5,4,3,2,1]

a = input()
last = a[8]
total = 0
#有可能為000000000
for i in range(8):
    total += int(a[i])*muti[i]
remainder = abs(10 - int(last))
if remainder == 10:
    remainder = 0
for i in range(65,91):
    ch = chr(i)
    if (total + int(dic[ch][0])*1 + int(dic[ch][1])*9) % 10 == remainder:
        print(ch,end = "")
