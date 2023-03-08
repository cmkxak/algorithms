from collections import deque
#미로탈출
n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))
dx=[-1,1,0,0] #상,하
dy=[0,0,-1,1] #좌,우

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        x,y= queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
        #미로 찾기 공간을 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
        #괴물이 존재하는 경우 [벽인 경우]
            if graph[nx][ny] == 0:
                continue
        # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                #벽뿌시기 -> 벽을 부셔가면서 이동 거리 값을 누적 하는 것(움직인 최단 거리를 구해주는 것)
                #기존 지점의 값 + 1
                graph[nx][ny] = graph[x][y] + 1 # 2로 값을 바꿔버림, 즉 방문 처리를 값을 바꿔줌으로써 조건문 안타게 하여 해버리는 것
                queue.append((nx,ny))
    return graph[n-1][m-1]

#BFS 결과 출력
print(bfs(0,0))