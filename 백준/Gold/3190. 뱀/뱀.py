def turn(direction, c):
    if c == "L":
        direction = (direction-1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 동 - 남 - 서 - 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
def simulate():
    #뱀의 시작 위치
    x,y = 1,1
    #시간 갱신 변수 선언
    time = 0
    #뱀이 머리 위치를 갱신하기 위한 리스트
    q = [(x,y)]
    #방향 전환 횟수 체크 인덱스
    idx = 0
    #방향을 지정하기 위한 변수
    direction = 0

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction] #뱀의 초기 방향 설정은 오른쪽

        if 1<=nx<=n and 1<=ny<=n and graph[nx][ny]!=2: #뱀이 자기 몸끼리 부딪히지 않고 범위 내에 있으면
            #이동한 자리에 사과가 없는 경우
            if graph[nx][ny] != 1:
                #뱀을 이동시킨다.
                graph[nx][ny] = 2
                #뱀이 차지하고 있는 위치 갱신
                q.append((nx,ny))
                #기존의 몸통 제거
                px,py = q.pop(0)
                graph[px][py] = 0
            #이동한 자리에 사과가 있는 경우
            else:
                graph[nx][ny] = 2
                q.append((nx,ny)) #뱀의 머리 위치 갱신
        #벽이나 뱀의 몸통에 부딪힌다면
        else:
            time+=1
            print(time)
            break
        x,y = nx,ny #이동한 위치로 x,y 갱신
        time+=1 #시간 증가

        if idx < l and time == int(dir[idx][0]):
            direction = turn(direction, dir[idx][1]) #방향 변환
            idx+=1 #방향 전환 횟수 증가

n=int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
k = int(input())
for i in range(k):
    x,y = map(int, input().split())
    graph[x][y] = 1
l = int(input())
dir = []
for i in range(l):
    dir.append(list(input().split()))
simulate()