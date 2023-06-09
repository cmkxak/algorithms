graph = [list(map(int, input().split())) for i in range(19)]

dir = [(1,0),(0,1),(-1,1), (1,1)]


def check_direction(x,y, stone):

    for k in range(4):
        cnt = 1
        nx = x + dir[k][0]
        ny = y + dir[k][1]

        while 0<= nx <19 and 0<=ny<19 and graph[nx][ny] == stone:
            cnt +=1
            
            if cnt == 5:
                #육목 체크
                if 0<= x - dir[k][0] < 19 and 0<= y - dir[k][1] < 19 and graph[x - dir[k][0]][y - dir[k][1]] == stone:
                    break
                if 0<= nx + dir[k][0] < 19 and 0<= ny + dir[k][1] < 19 and graph[nx + dir[k][0]][ny + dir[k][1]] == stone:
                    break
                print(stone)
                print(x+1, y+1)
                exit()
            nx,ny = nx + dir[k][0], ny+dir[k][1]

for x in range(19):
    for y in range(19):
        if graph[x][y] == 1:
            check_direction(x,y,1)

        elif graph[x][y] == 2:
            check_direction(x,y,2)

print(0)