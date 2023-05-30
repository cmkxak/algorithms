import sys
input = sys.stdin.readline

n,k = map(int, input().split())
nums = list(map(int, input().split()))
prefix_sum = [sum(nums[:k])]
tmp = 0

for i in range(1, n-k+1):
    prefix_sum.append(prefix_sum[i-1] - nums[i-1] + nums[k+i-1])
print(max(prefix_sum))