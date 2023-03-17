import sys
input=sys.stdin.readline

n,m=map(int,input().split())
nums=list(map(int, input().split()))
nums.sort()
res=[]
def func():
    if len(res) == m:
        print(*res)
        return
    tmp=0
    for i in range(n):
        if not checked[i] and tmp != nums[i]:
            checked[i]=True
            res.append(nums[i])
            tmp=nums[i]
            func()
            res.pop()
            checked[i]=False
checked=[False] * n
func()