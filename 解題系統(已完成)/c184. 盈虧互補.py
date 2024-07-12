def solve(num,time):
    time += 1
    if num == 1:
        print("=0")
        print(f"{n} has no friends.")
    else:
        total = 1
        list = [1]
        for i in  range(2,int(num**0.5)+1):
            if num % i == 0:
                total += i + num // i
                list.append(i)
                list.append(num // i)
        list.sort()
        first = list.pop(0)
        print(first, end="")
        while list:
            a = list.pop(0)
            print(f"+{a}", end="")
        print(f"={total}")
        if total == num: print(f"{num} is perfect.")
        else:
            if time == 2:
                if n == total:
                    print(f"{n} and {num} are friends.")
                else:
                    print(f"{n} has no friends.")
            else:
                solve(total, time )

n = int(input())
solve(n,0)
