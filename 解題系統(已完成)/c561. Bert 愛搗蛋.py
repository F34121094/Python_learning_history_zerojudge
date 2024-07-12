n = int(input())

a = input().split()
rever_list = [item[::-1] for item in a]
final = max(list(map(int,rever_list)))
print(final)