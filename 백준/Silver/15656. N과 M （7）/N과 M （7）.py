import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int, input().split()))
arr.sort()
nums=[]
def func():
    if len(nums) == m:
        print(*nums)
        return
    for i in range(n):
        nums.append(arr[i])
        func()
        nums.pop()
func()