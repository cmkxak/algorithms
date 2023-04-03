import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
adj_list = [[] for _ in range(n + 1)] #인접 리스트
visited = [-1] * (n+1)

for _ in range(m):
    s,e = map(int, input().split())
    adj_list[s].append(e)

def bfs(start):
    queue=deque()
    queue.append(start)
    visited[start]+=1

    while queue:
        now_node = queue.popleft()

        for new_node in adj_list[now_node]:
            if visited[new_node] == -1:
                queue.append(new_node)
                visited[new_node] = visited[now_node] + 1
bfs(x)
result = []
for i in range(n+1):
    if visited[i] == k:
        result.append(i)
if result:
    for i in result:
        print(i)
else:
    print(-1)