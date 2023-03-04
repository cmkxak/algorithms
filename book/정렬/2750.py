import sys
input=sys.stdin.readline
n=int(input())
nums=[int(input()) for i in range(n)]
for i in range(n-1):
    for j in range(n-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
for i in nums:
    print(i)
    