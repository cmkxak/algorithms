n,m = map(int, input().split())
visited = [False] * (n+1)
nums = []

def dfs():

    if len(nums) == m:
        print(*nums)
        return

    for i in range(1,n+1):
        visited[i] = True
        nums.append(i)
        dfs()
        nums.pop()
        visited[i] = False
dfs()