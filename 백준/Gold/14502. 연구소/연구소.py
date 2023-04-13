from itertools import combinations
from collections import deque
import copy
import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(w1,w2,w3):
    tmp = copy.deepcopy(graph)
    tmp[w1[0]][w1[1]] = 1
    tmp[w2[0]][w2[1]] = 1
    tmp[w3[0]][w3[1]] = 1

    queue = deque()
    for i, j in virus:
        queue.append((i, j))

    answer = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and tmp[nx][ny] != 1:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = 2  # 바이러스 전파
                    queue.append((nx, ny))
    for i in range(m):
        for j in range(n):
            if tmp[i][j] == 0:
                answer += 1
    return answer

m, n = map(int, input().split())
graph = []
for i in range(m):
    graph.append(list(map(int, input().split())))

virus = []
wall = []

for i in range(m):
    for j in range(n):
        if graph[i][j] == 2:
            virus.append((i, j))
        if graph[i][j] == 0:
            wall.append((i, j))

wall_list = list(combinations(wall, 3))
result = 0
for i, j, k in wall_list:
    ans = bfs(i,j,k)
    result = max(result, ans)
print(result)