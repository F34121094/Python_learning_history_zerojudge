n= int(input())

a = input()
num_list = list(map(int,a.split()))
num_list.sort()
print(*num_list)
set_list = list(set(num_list))
set_list.sort(reverse = True)
print(*set_list)