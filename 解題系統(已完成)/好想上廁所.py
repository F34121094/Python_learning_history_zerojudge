amount = int(input())

restroom = [[],[]]
for _ in range(amount):
    restroom[0].append(0)
    restroom[1].append(0)
while 1:
    try:
        time = 0
        a,b = map(int,input().split())
        i = 0
        #1
        for i in range(0,amount):
            if restroom[1][i] == 0:
                if i == 0:
                    if restroom[1][1] == 0:
                        restroom[0][i] = a
                        restroom[1][i] = b
                        time+=1
                        print(f"Number:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[0][j], end="")
                        print()
                        print(f"  Time:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[1][j], end="")
                        break
                if i != amount-1:
                    if restroom[1][i-1] == 0 and restroom[1][i+1] == 0:
                        restroom[0][i] = a
                        restroom[1][i] = b
                        time +=1
                        print(f"Number:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[0][j], end="")
                        print()
                        print(f"  Time:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[1][j], end="")
                        break
                else:
                    if restroom[1][amount-2] == 0:
                        restroom[0][i] = a
                        restroom[1][i] = b
                        time += 1
                        print(f"Number:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[0][j], end="")
                        print()
                        print(f"  Time:", end='')
                        for j in range(amount):
                            print(" ", end='')
                            print(restroom[1][j], end="")
                        break
            #第二次找前後其中一個是0
        #2
        # if time ==0:
        #     for i in range(1,amount-1):
        #         if restroom[1][i] == 0:
        #             if restroom[1][i-1] == 0 or restroom[1][i+1] == 0:
        #                 restroom[0][i] = a
        #                 restroom[1][i] = b
        #                 time += 1
        #                 print(f"Number:", end='')
        #                 for j in range(amount):
        #                     print(" ", end='')
        #                     print(restroom[0][j], end="")
        #                 print()
        #                 print(f"  Time:", end='')
        #                 for j in range(amount):
        #                     print(" ", end='')
        #                     print(restroom[1][j], end="")
        #                 break
        #3
        if time ==0:
            for i in range(0,amount):
                if restroom[1][i] == 0:
                    time +=1
                    restroom[0][i] = a
                    restroom[1][i] = b
                    print(f"Number:", end='')
                    for j in range(amount):
                        print(" ", end='')
                        print(restroom[0][j], end="")
                    print()
                    print(f"  Time:", end='')
                    for j in range(amount):
                        print(" ", end='')
                        print(restroom[1][j], end="")
                    break
        #not enough
        if time == 0 :

            print("Not enough")
            print(f"Number:", end='')
            for j in range(amount):
                print(" ", end='')
                print(restroom[0][j], end="")
            print()
            print(f"  Time:", end='')
            for j in range(amount):
                print(" ", end='')
                print(restroom[1][j], end="")
        for i in range(amount):
            if restroom[1][i] != 0: restroom[1][i] -= 1

            if restroom[1][i] == 0:
                restroom[0][i] = 0
        print()
        print()


    except:
        break