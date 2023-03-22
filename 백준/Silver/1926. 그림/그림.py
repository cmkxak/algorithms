# 그림
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt
    # 넓이 계산을 위한 변수
    distance = 1

    # 시작점 방문 처리
    graph[x][y] = 0

    # 시작점 큐에 삽입
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0  # 방문 처리
                queue.append((nx, ny))  # 방문 처리 후 큐에 삽입
                distance += 1
    return distance

cnt=0
result=0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt+=1
            result=max(result, bfs(i,j))
print(cnt)
print(result)
