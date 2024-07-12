
while 1:
    try:
        n = input()
        total = 0
        for i in range(len(n)):
            if n[i] == '0' or n[i] == '6' or n[i] == '9':
                total += 1
            elif n[i] == '8':
                total += 2
            else: continue
        print(total)
    except:
        break
