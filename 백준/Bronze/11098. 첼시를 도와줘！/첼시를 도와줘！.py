n=int(input())
res=[]
for i in range(n):
    t=int(input())
    max=0
    for j in range(t):
        info = input().split()
        res.append(info)
        if int(res[j][0]) > max:
            max=int(res[j][0])
            max_idx = j

    print(res[max_idx][1])
    res.clear()
