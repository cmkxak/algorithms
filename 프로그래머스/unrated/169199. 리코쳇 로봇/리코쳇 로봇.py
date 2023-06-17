from collections import deque

dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(i,j,board,visited):
    answer = 1
    queue =deque()
    queue.append((i,j))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<len(board) and 0<=ny<len(board[0]):
                if board[nx][ny] == 'G':
                    break
                if board[nx][ny] == 'D':
                    break
                if board[nx][ny] == '.' and not visited[nx][ny]:
                    print(nx,ny)
                    visited[nx][ny] = 1
                    queue.append((nx,ny))
                    answer+=1
    return answer
            
def solution(board):
    answer = -1
    
    visited = [[0] * len(board[0]) for i in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs(i,j,board,visited)
    return answer