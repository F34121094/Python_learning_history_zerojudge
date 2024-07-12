while 1:
    try:
        read = input()
        total = 0
        if "hour" in read:
            read = read.split("hour")
            total += int(read[0]) * 3600000
            print(total)
            continue

        if "min" in read:
            read = read.split("min")
            total += int(read[0]) * 60000
            print(total)
            continue

        if "h" in read:
            read = read.split("h")
            total += int(read[0]) * 3600000
            read.pop(0)
            read = "".join(read)

        if "ms" in read:
            read = read.split("ms")
            check = read[0]
            if "s" in check:
                check = check.split("s")
                total += int(check[1])
                check.pop(1)
                read = check[0]+"s"
            elif "m" in check:
                check = check.split("m")
                total += int(check[1])
                check.pop(1)
                read = check[0]+"m"
            else:
                total += int(check)
                print(total)
                continue

        if "m" in read:
            read = read.split("m")
            total += int(read[0]) * 60000
            read.pop(0)
            read = "".join(read)

        if "s" in read:
            read = read.split("s")
            total += int(float(read[0]) * 1000)
            read.pop(0)
            read = "".join(read)


        print(total)
    except:
        break