from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def bfs(start,visited,graph):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        x = queue.popleft()

        print(x, end = ' ')

        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

def dfs(graph, visited,i):
    visited[i] = True

    print(i, end=' ')

    for k in graph[i]:
        if not visited[k]:
            visited[k] = True
            dfs(graph, visited, k)

n,m,s = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited= [False] * (n+1)
visited2= [False] * (n+1)

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(graph,visited,s)
print()
bfs(s,visited2,graph)