from collections import deque
import sys
input = sys.stdin.readline

def bfs(start, dist):
    answer = []
    queue = deque()
    queue.append((start, dist))
    visited[start] = True

    while queue:
        x,dist = queue.popleft()

        if dist == k:
            answer.append(x)

        for i in adj_list[x]:
            if not visited[i]:
                visited[i] = True
                queue.append((i, dist+1))
    return answer

n,m,k,x= map(int, input().split())
adj_list = [[] for _ in range(n+1)] #인접 리스트

for i in range(m):
    s,e = map(int, input().split())
    adj_list[s].append(e)

visited = [False] * (n+1)

result = bfs(x, 0)

result.sort()
if result:
    for i in result:
        print(i)
else:
    print(-1)