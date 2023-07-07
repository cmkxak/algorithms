n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()
s,e = 0,n-1
cnt = 0
while s<e:
    if nums[s] + nums[e] == m:
        cnt += 1
        s+=1
        e-=1
    elif nums[s] + nums[e] > m:
        e-=1
    else:
        s+=1
print(cnt)