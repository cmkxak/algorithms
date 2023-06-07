n = int(input())
m = int(input())

graph = [[0] * (n) for i in range(n)]

#시작점 초기화
x = (n-1)//2
y = (n-1)//2
graph[x][y] = 1

#상하좌우 좌표설정
dx = [-1,1,0,0]
dy = [0,0,-1,1]

i = 2
start = 3

while x != 0 and y != 0:
    #이동 횟수 정의
    while i <= start * start:
        if x == (n-1)//2 and y == (n-1)//2: #시작점 이라면 n이 5일 경우, (2,2) => (1,1)에서 종료
            up, down, left, right = start, start-1, start-1, start-2 #시작점마다 위,아래,왼쪽,오른쪽 이동 횟수 갱신
            x = x + dx[0]
            y = y + dy[0]
            up -=1

        elif right > 0:
            x = x + dx[3]
            y = y + dy[3]
            right-=1

        elif down > 0:
            x = x + dx[1]
            y = y + dy[1]
            down-=1

        elif left > 0:
            x = x + dx[2]
            y = y + dy[2]
            left-=1

        elif up > 0:
            x = x + dx[0]
            y = y + dy[0]
            up-=1

        graph[x][y] = i
        i+=1

    n-=2 #시작점 감소
    start += 2
answer = []
for i in graph:
    print(*i)
    if m in i:
        answer.extend((graph.index(i) + 1, i.index(m) + 1))
if answer:
    print(*answer)