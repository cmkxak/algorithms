from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<m and 0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
    cnt+=1

t=int(input())
for _ in range(t):
    cnt=0
    m,n,k = map(int,input().split())
    graph=[[0] * (n) for _ in range(m)]

    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    for x in range(m):
        for y in range(n):
            if graph[x][y] == 1:
                bfs(x,y)
    print(cnt)