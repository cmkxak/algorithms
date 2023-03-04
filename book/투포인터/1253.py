# 좋은 수
import sys
input = sys.stdin.readline
count = 0
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
for i in range(n):
    s = 0
    e = n-1
    k = nums[i]
    while s < e:
        if nums[s]+nums[e]==k:
            # 서로 다른 수의 합으로 나타내야 하므로
            if s != k and e != k:
                count += 1
                break
            elif s == k:
                s += 1
            elif e == k:
                e -= 1
        elif nums[s] + nums[e] < k:
            s += 1
        else:
            e -= 1
print(count)
