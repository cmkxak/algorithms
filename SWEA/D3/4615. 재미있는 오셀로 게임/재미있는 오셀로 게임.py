t = int(input())
direction = ((0,1), (0,-1), (-1,0), (1,0), (-1,1), (1,1), (-1,-1), (1,-1))

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    info = []
    graph = [[0] * (n) for i in range(n)]
    for _ in range(m):
        x, y, stone = map(int, input().split())
        info.append((x, y, stone))
    # 1. 그래프 초기화
    graph[n // 2 - 1][n // 2 - 1] = 2
    graph[n // 2 - 1][n // 2] = 1
    graph[n // 2][n // 2 - 1] = 1
    graph[n // 2][n // 2] = 2

    # 2. 돌 두기 - 자르지 말고 시뮬레이션 이용해야 함 by 방향벡터
    for x,y,stone in info:
        x,y = x-1, y-1
        reverse = [] #뒤집어야 할 돌 리스트들을 담아줄 리스트
        for i in range(8):
            nx = x + direction[i][0]
            ny = y + direction[i][1]
            while True:
                #모서리 체크
                if nx < 0 or ny < 0 or nx >= n or ny>=n:
                    reverse = []
                    break

                #빈칸을 만나는 경우
                if graph[nx][ny] == 0:
                    reverse = []
                    break

                #같은 색을 만나는 경우
                if graph[nx][ny] == stone:
                    break
                #다른 색을 만나는 경우
                else:
                    reverse.append((nx,ny))
                nx,ny = nx+direction[i][0], ny+direction[i][1]

            #방향에서 다른 것들을 뒤집어주기
            for rx,ry in reverse:
                if stone == 1:
                    graph[rx][ry] = 1
                elif stone == 2:
                    graph[rx][ry] = 2
        graph[x][y] = stone #시작 지점에 돌 배치
    black, white = 0,0
    for i in graph:
        black+= i.count(1)
        white+= i.count(2)
    print("#{} {} {}".format(tc, black, white))