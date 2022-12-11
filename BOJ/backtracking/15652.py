n,m = map(int, input().split())
visited = [False] * (n+1)
nums = []

def dfs(start):
    if len(nums) == m:
        print(*nums)
        return

    for i in range(start,n+1):
        visited[i]=True
        nums.append(i)
        dfs(i)
        nums.pop()
        visited[i] = False
dfs(1)