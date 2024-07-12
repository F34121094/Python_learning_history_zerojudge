a ,b = map(int,input().split())
a_even = a%2#0為偶機為1
b_even = b%2
gap = b-a
total = gap
if a_even == 0 and b_even == 1:print((gap + 1)//2)
elif a_even == 1 and b_even == 0:print((gap + 1) // 2)
elif a_even == 0 and b_even == 0: print(gap//2 + 1)
else:print(gap//2)