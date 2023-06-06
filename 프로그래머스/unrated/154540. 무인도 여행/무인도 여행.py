from collections import deque

dx = [-1,1,0,0] #행
dy = [0,0,-1,1] #열

def bfs(x,y,maps,visited):
    sum = int(maps[x][y])
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            
            if maps[nx][ny] != 'X':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    sum += int(maps[nx][ny])
                    queue.append((nx,ny))
    return sum 
    
def solution(maps):
    answer = []
    visited = [[False] * len(maps[0]) for i in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X':
                if not visited[i][j]:
                    visited[i][j] = True
                    answer.append(bfs(i,j,maps,visited))
    if answer:
        return sorted(answer)
    else:
        return [-1]