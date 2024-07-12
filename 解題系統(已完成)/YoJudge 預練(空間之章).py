while 1:
    try:
        read = input()
        total = 0
        if "gb" in read:
            read = read.split("gb")
            total += int(read[0]) * 8000000000
            print(total)
            continue

        if "mb" in read:
            read = read.split("mb")
            total += int(read[0]) * 8000000
            print(total)
            continue
        if "kb" in read:
            read = read.split("kb")
            total += int(float(read[0]) * 8000)
            print(total)
            continue
        if "byte" in read:
            read = read.split("byte")
            check = read[0]
            if "." in check:
                check = check.split(".")
                total += int(check[0])*8 + int(check[1])
            else: total += int(float(read[0]) * 8)
            print(total)
            continue
        if "bit" in read:
            read = read.split("bit")
            total += int(read[0])
            print(total)
            continue

        if "g" in read:
            read = read.split("g")
            total += int(read[0]) * 8000000000
            read.pop(0)
            read = "".join(read)


        if "m" in read:
            read = read.split("m")
            total += int(read[0]) * 8000000
            read.pop(0)
            read = "".join(read)

        if "k" in read:
            read = read.split("k")
            total += int(float(read[0]) * 8000)
            read.pop(0)
            read = "".join(read)


        print(total)
    except:
        break