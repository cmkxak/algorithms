import copy

t = int(input())

for _ in range(t):
    n, d= map(int, input().split())

    #배열 입력
    graph = [list(map(int, input().split())) for i in range(n)]

    #각도가 양수인 경우
    if d >= 45:
        #반복 횟수 지정
        repeat = d // 45
        for _ in range(repeat):
            new_graph = copy.deepcopy(graph)

            #x의 주대각선 to 가운데열
            for j in range(n):
                new_graph[j][((n+1)//2) -1] = graph[j][j]

            #x의 가운데열 to x의 부대각선
            for j in range(n):
                new_graph[n-j-1][j] = graph[n-j-1][((n+1)//2) -1]

            #x의 부대각선 to x의 가운데 행
            for j in range(n):
                new_graph[((n+1)//2) -1][j] = graph[n-j-1][j]

            #x의 가운데 행 to x의 주 대각선
            for j in range(n):
                new_graph[j][j] = graph[((n+1)//2) -1][j]

            #회전한 배열로 업데이트
            graph = new_graph
    #각도가 음수인 경우
    else:
        repeat = abs(d) // 45
        for _ in range(repeat):
            new_graph = copy.deepcopy(graph)

            #x의 주대각선 to 가운데 행 (앞이 원래 그래프)
            for i in range(n):
                new_graph[((n+1)//2) -1][i] = graph[i][i]

            #x의 가운데열 to 주대각
            for i in range(len(graph)):
                new_graph[i][i] = graph[i][((n+1)//2) -1]

            #x의 가운데 행 to 부대각
            for i in range(len(graph)):
                new_graph[n-i-1][i] = graph[((n+1)//2) -1][i]

            #x의 부대각선 to 가운데열
            for i in range(len(graph)):
                new_graph[i][((n+1)//2) -1] = graph[i][n-i-1]

            #그래프 갱신
            graph = new_graph

    for i in graph:
        print(*i)