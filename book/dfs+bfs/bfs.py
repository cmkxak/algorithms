from collections import deque

def bfs(graph, visited, node):
    #큐를 하나 생성
    queue=deque([node])

    #현재 노드 방문 처리
    visited[node]=True

    #큐가 빌떄까지 반복
    while queue:
        #큐에서 원소 하나를 뽑는다.
        v=queue.popleft()
        print(v, end=' ')
        #큐에서 꺼낸 정점의 인접 정점들을 순회
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
graph=[
    [],#0
    [2,3,8],#1
    [1,7],#2
    [1,4,5],#3
    [4,5],#4
    [3,4],#5
    [7],#6
    [2,6,8],#7
    [1,7]#8
]
#각 노드가 방문된 정보 표현(1차원 리스트)
visited=[False]*9
bfs(graph, visited, 1)
