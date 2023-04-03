import copy
from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]
result = 0

def get_score(graph):
    score = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                score +=1
    return score

dx=[-1,1,0,0]
dy=[0,0,-1,1]
#벽 세개 완성되었으면 바이러스의 위치에서 전파 시작
def virus():
    global result
    queue=deque()
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append((nx,ny))
    result = max(result, get_score(tmp_graph))
    return result

def makeWall(cnt):
    if cnt == 3:
        virus()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1 #벽 설치
                makeWall(cnt+1)
                graph[i][j] = 0
makeWall(0)
print(result)