#n,m의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램
from collections import deque

n,m = map(int, input().split())
graph = list(list(map(int, input())) for _ in range(n))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1:
                    queue.append((nx,ny))
                    graph[nx][ny] = graph[x][y] + 1
                else:
                    continue
    return graph[n-1][m-1]

print(bfs(0,0))