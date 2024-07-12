tool = {
    "+":5,"-":5,"*":9,"/":9,"(":-1,")":-1,"%":9
}
while 1:
    try:
        str = input().split()
        for i in range(len(str)):
            if str[i] not in tool:
                str[i] = int(str[i])    #轉變成功
        postfix = []
        stack = []

        while len(str) != 0:
            a = str.pop(0)
            if a not in tool:
                postfix.append(a)
            else:
                if a == "(":
                    stack.append(a)
                elif a == ")":
                    while stack[len(stack)-1] != "(":
                        a = postfix.pop()
                        b = postfix.pop()
                        c = stack.pop()
                        if c == "+":
                            result = a + b
                        elif c == "-":
                            result = a - b
                        elif c == "*":
                            result = a * b
                        elif c == "/":
                            result = b // a
                        elif c == "%":
                            result = b % a
                        postfix.append(result)
                    stack.pop()
                else:
                    if len(stack) == 0: stack.append(a)
                    elif tool[a] >= tool[stack[len(stack)-1]] : stack.append(a)
                    else:
                        while tool[a] < tool[stack[len(stack) - 1]]:
                            a = postfix.pop()
                            b = postfix.pop()
                            c = stack.pop()
                            if c == "+":
                                result = a + b
                            elif c == "-":
                                result = a - b
                            elif c == "*":
                                result = a * b
                            elif c == "/":
                                result = b // a
                            elif c == "%":
                                result = b % a
                            postfix.append(result)
                            if len(stack) == 0:
                                break

        while stack:
            a = postfix.pop()
            b = postfix.pop()
            c = stack.pop()
            if c == "+": result = a+b
            elif c == "-": result = a - b
            elif c == "*": result = a * b
            elif c == "/":
                result = b // a
            elif c == "%":
                result = b % a
            postfix.append(result)



        print(postfix[0])
    except:
        break