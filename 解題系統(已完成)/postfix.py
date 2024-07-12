cha = ['a','b','c','d','e','f','g','h','i','j','k',
       'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dic = {
    '(':-1,
    '+':1,'-':1,
    '*':2,'/':2}

while 1:
    try:
        read = input().split()
        if not read : break
        stack = []
        postfix =[]
        for i in range(len(read)):
            if read[i] in cha: postfix.append(read[i])

            else: #只處理operator
                if len(stack) == 0:
                    stack.append(read[i])
                    continue

                if read[i] == "(":
                    stack.append(read[i])
                    continue

                if read[i] == ")":
                    while stack[-1] != "(":
                        postfix.append(stack.pop())
                    stack.pop()#刪掉 (
                    continue

                if dic[read[i]] <= dic[stack[-1]]:
                    while 1:
                        postfix.append(stack.pop())
                        if stack == [] or dic[read[i]] > dic[stack[-1]]: break
                    stack.append(read[i])

                else: stack.append(read[i])

        while stack:
            postfix.append(stack.pop())

        print(*postfix)

    except:
        break