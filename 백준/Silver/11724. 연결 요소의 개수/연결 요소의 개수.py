import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000);

def dfs(n):
    visited[n] = True

    for i in graph[n]:
        if not visited[i]:
            dfs(i)

n,m = map(int, input().split())
graph = [[] for i in range(1, n+2)]
visited = [False] * (n+2)

for i in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count+=1
        dfs(i)
print(count)