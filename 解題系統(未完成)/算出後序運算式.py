dic = ["+","-","*","/"]
def cal(read,i):
    if len(read) == 1:
        return read[0]

    if read[i] in dic:
        a = int(read[i-2])
        b = int(read[i-1])
        if read[i] == "+": total = a + b
        elif read[i] == "-": total = a - b
        elif read[i] == "*": total = a * b
        elif read[i] == "/": total = a / b

        del read[i-2 : i+1]     #刪除i-2到 i
        read.insert(i-2, int(total))
        if len(read) == 1:
            return int(read[0])
        else : return cal(read, i - 1,)
    else:
        if len(read) == 1:
            return int(read[0])
        else : return cal(read, i + 1 )


read = input().split()
i = 0
ans = cal(read,i)
print(ans)

