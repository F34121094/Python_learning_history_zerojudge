def solve(arr,num_now):
    if arr[num_now]:
        i = arr[num_now].pop()
    elif any(arr):
        print("NO")
        return
    else:
        print("YES")
        return

    arr[i - 1].remove(num_now + 1)
    solve(arr, i-1)

while 1:
    try:
        read = input().split()
        if not read:
            continue
        n,m = int(read[0]),int(read[1])
        num_to_next = [[] for i in range(n)]
        for i in range(m):
            a,b = map(int,input().split())
            num_to_next[a-1].append(b)
            num_to_next[b-1].append(a)

        solve(num_to_next,0)
    except:
        break