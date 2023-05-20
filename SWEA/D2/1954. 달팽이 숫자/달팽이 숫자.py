t = int(input())

#우 하 좌 상
dr = [0,1,0,-1]
dc = [1,0,-1,0]
for test_case in range(1, t+1):
    n = int(input())
    graph = [[0] * n for i in range(n)]
    x,y = 0,0
    dist = 0

    for i in range(1, n*n+1):
        graph[x][y] = i
        x += dr[dist]
        y += dc[dist]

        if x < 0 or y < 0 or x >= n or y >=n or graph[x][y] != 0:
            x-=dr[dist]
            y-=dc[dist]

            dist = (dist + 1) % 4 #방향 전환

            x+=dr[dist]
            y+=dc[dist]

    print("#{}".format(test_case))
    for i in graph:
        print(*i)