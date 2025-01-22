from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j,board,cnt,visited):
    queue =deque()
    queue.append((i,j,cnt))
    
    while queue:
        x,y,c = queue.popleft()
        if board[x][y] == 'G':
            return c
        
        for i in range(4): # 0 6
            nx = x
            ny = y
            while 0<= nx + dx[i] <len(board) and 0<= ny+dy[i] < len(board[0]) and board[nx+dx[i]][ny+dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
                
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx,ny, c + 1))
    return -1
            
def solution(board):
    answer = 0
    
    visited = [[0] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs(i,j,board,0,visited)
    return answer