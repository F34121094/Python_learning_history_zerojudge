n = int(input())
for _ in range(n):
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"Case {_+1}: a leap year")
    else: print(f"Case {_+1}: a normal year")