think = input()
T = int(input())
for i in range(T):
    read = input()
    a = 0
    b = 0
    for j in range(4):
        if think[j] == read[j]:
            a+=1
            continue
        elif read[j] in think:
            b +=1
    print(f"{a}A{b}B")