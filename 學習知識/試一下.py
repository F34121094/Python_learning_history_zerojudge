dic = ["+", "-", "*", "/"]


def cal(read, i=0):
    if len(read) == 1:
        return int(read[0])

    if read[i] in dic:
        # 获取操作数
        a = int(read[i - 2])
        b = int(read[i - 1])
        # 根据运算符进行计算
        if read[i] == "+": total = a + b
        elif read[i] == "-": total = a - b
        elif read[i] == "*": total = a * b
        elif read[i] == "/": total = a / b
        # 删除已使用的操作符和操作数
        del read[i - 2:i + 1]
        # 插入计算结果
        read.insert(i - 2, str(total))
        # 递归调用进行下一轮计算
        return cal(read, i - 1)
    else:
        # 没有运算符，继续递归
        return cal(read, i + 1)


read = input().split()
result = cal(read)
print(result)