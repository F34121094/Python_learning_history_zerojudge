while 1:
    try:
        str = input()
        max_num = 0
        max_ch = str[0]
        current_num = 1
        for i in range(1,len(str)):
            if str[i] != str[i-1]:
                if current_num > max_num:
                    max_num = current_num
                    current_num = 1
                    max_ch = str[i-1]
                    continue
                else:
                    current_num = 1
                    continue
            else:
                current_num += 1
        if current_num > max_num:
            max_num = current_num
            max_ch = str[-1]
        print(f"{max_ch} {max_num}")
    except:
        break