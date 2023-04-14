n= int(input())
e =int(input())
graph = [[] * n for _ in range(n+1)]
for _ in range(e):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
count = 0 
visited = [0] * (n+1)
def dfs(v):
  global count
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
        dfs(i)
        count+=1
dfs(1)
print(count)
