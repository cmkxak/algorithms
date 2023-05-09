import sys
import heapq
input=sys.stdin.readline
n=int(input())
nums = []

for i in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(nums, -num)
    else:
        if len(nums) == 0:
            print(0)
        else:
            print(-heapq.heappop(nums))