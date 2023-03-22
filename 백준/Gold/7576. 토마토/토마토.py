from collections import deque
m,n=map(int,input().split())

graph=[list(map(int, input().split())) for _ in range(n)]

#시작점이 여러 개 일 수도 있으므로, 미리 큐에 삽입
queue=deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs():
    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))

bfs()
max_res=0
for row in graph:
    for i in row:
        if i == 0:
            print(-1)
            exit(0)
        #각 행의 열을 일일이 탐색하며, 최댓값을 구해주고 기존의 최댓값과 비교하여 최소 날짜를 구해준다.
        max_res=max(max_res,i)
print(max_res-1)