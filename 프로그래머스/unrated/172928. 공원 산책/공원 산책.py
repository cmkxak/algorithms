
def check(x,y,park):
    if x<0 or y<0 or x>=len(park) or y>=len(park[0]):
        return True
    if park[x][y] == 'X':
        return True
    return False

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def move(x,y,park,routes):
    for route in routes:
        dir = route[0]
        recur = int(route[2])
        
        prev_x, prev_y = x,y
        
        if dir == 'N':
            for i in range(recur):
                nx = x + dx[0]
                ny = y + dy[0]
                if check(nx,ny,park):
                    x,y = prev_x, prev_y
                    break
                else:
                    x,y = nx,ny
        
        elif dir == 'S':
            for i in range(recur):
                nx = x + dx[1]
                ny = y + dy[1]
                if check(nx,ny,park):
                    x,y = prev_x, prev_y
                    break
                else:
                    x,y = nx, ny
        
        elif dir == 'E':
            for i in range(recur):
                nx = x + dx[3]
                ny = y + dy[3]
                if check(nx,ny,park):
                    x,y = prev_x, prev_y
                    break
                else:
                    x,y = nx,ny
        
        elif dir == 'W':
            for i in range(recur):
                nx= x + dx[2]
                ny= y + dy[2]
                if check(nx,ny,park):
                    x,y = prev_x, prev_y
                    break
                else:
                    x,y = nx,ny
    return x,y       
        
def solution(park, routes):
    answer = []
    for i,p in enumerate(park):
        park[i] = list(p)
        
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x,y=move(i,j,park,routes)        
                answer.append(x)
                answer.append(y)
    return answer