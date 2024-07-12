#第一行為正確密碼
#第二行為n次
#pAqB p為正確值+位置 q僅正確值
def check_p(correct, type):
    time = 0
    a = []
    for i in range(len(correct)):
        if correct[i] == type[i]:
            time += 1
            a = [i] + a
        else:
            continue
    for i in a:
        correct = correct[:i] + correct[i+1:]
        type = type[:i] + type[i+1:]
    return time,correct,type
def check_q(correct, type):
    # print(correct,type)
    time = 0
    for i in range(len(type)):
        time += correct.count(type[i])
    return time

while 1:
    try:
        correct = list(map(str, input().rstrip().split()))
        n = int(input())
        for i in range(n):
            correct_copy = correct[:]
            # print(correct_copy)
            type = list(map(str, input().rstrip().split()))
            p ,correct_copy ,type = check_p(correct_copy,type)
            q = check_q(correct_copy,type)
            print(f"{p}A{q}B")
    except:
        break
