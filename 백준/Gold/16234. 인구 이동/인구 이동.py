import sys
from collections import deque
input = sys.stdin.readline
# 인구이동이 없을 때 까지 반복
# 모든 곳을 bfs로 방문하여 연합 진행
# 인접 국가를 탐색하면서 인구 차이가 l명 이상 r명 이하인 경우 연합 진행
# 연합 국가 간 인구수는 (연합의 인구수 / 연합을 이루고 있는 칸의 개수)가 되도록 계산
# 지금까지 인구 이동이 없는 경우 그만

n,l,r = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(a,b):
    union_val = graph[a][b]
    union_country = [(a,b)]
    queue=deque()
    queue.append((a,b))

    #인접 국가를 탐색하면서 인구 차이가 l명이상 r명 이하인 경우 연합 국가에 담기
    while queue:
        x,y= queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if l <= abs(graph[x][y]-graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    union_country.append((nx, ny))
                    queue.append((nx, ny))
                    union_val += graph[nx][ny]
    return union_val, union_country

cnt=0
while True: #인구 이동이 없을 때까지 반복
    visited = [[False] * (n) for _ in range(n)]
    moved = False #인구 이동 존재 유무 플래그

    #모든 곳을 bfs로 방문하여 연합 진행
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                union_val, union_country = bfs(i, j)

                if len(union_country) > 1:
                    moved = True
                    for x,y in union_country:
                        graph[x][y] = union_val // len(union_country)
    if moved:
        cnt+=1
    else:
        break
print(cnt)