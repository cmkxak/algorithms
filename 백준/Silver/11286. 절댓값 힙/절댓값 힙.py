import sys
import heapq
input=sys.stdin.readline
t=int(input())
nums = []
for i in range(t):
    num = int(input())
    if num !=0:
        heapq.heappush(nums, (abs(num), num))
    else:
        if not nums:
            print(0)
        else:
            print(heapq.heappop(nums)[1])
