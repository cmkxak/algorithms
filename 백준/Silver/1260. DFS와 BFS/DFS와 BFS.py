from collections import deque
def dfs(adj,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in adj[v]:
        if not visited[i]:
            dfs(adj,i,visited)

def bfs(adj,v,visited):
    queue = deque([v])
    visited = [False] * (n+1)
    visited[v] = True
    while queue:
        vertex = queue.popleft()
        print(vertex, end = ' ')
        for i in adj[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    a = input().split()
    adj[int(a[0])].append(int(a[1]))
    adj[int(a[1])].append(int(a[0]))

visited = [False] * (n+1)

for i in adj:
    i.sort()
dfs(adj,v,visited)
print()
bfs(adj,v,visited)