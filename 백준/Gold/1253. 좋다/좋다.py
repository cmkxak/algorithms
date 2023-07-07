import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

nums.sort()
answer = 0
for i in range(len(nums)):
    s,e = 0,n-1
    while s < e:
        if nums[s] + nums[e] == nums[i]:
            if s != i and e !=i:
                answer += 1
                break
            elif s == i:
                s+=1
            elif e == i:
                e-=1
                
        elif nums[s] + nums[e] < nums[i]:
            s+=1
        else:
            e-=1
print(answer)