from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j,maps,visited,sum):
    queue = deque()
    queue.append((i,j))   
    while queue:
        x,y = queue.popleft()      
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]          
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] != 1:
                    sum+= int(maps[nx][ny])
                    queue.append((nx,ny))
                    visited[nx][ny] = 1
    return sum
        
def solution(maps):
    answer = [] 
    r,c = len(maps), len(maps[0])
    visited = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = 1
                sum = int(maps[i][j])
                result = bfs(i,j,maps,visited,sum)
                answer.append(result)
    if not answer:
        return [-1]
    else:
        return sorted(answer)
