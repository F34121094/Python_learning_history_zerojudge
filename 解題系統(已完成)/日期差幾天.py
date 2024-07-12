import datetime
from sys import stdin

for read in stdin:
    a = [int(i) for i in read.split()]
    b = [int(i) for i in input().split()]
    day_1 = datetime.datetime(a[0],a[1],a[2])
    day_2 = datetime.datetime(b[0], b[1], b[2])
    print(abs((day_1 - day_2).days))
