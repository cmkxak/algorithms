import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드, 간선 개수 입력받기
n,m = map(int, input().split())

#시작 노드 입력받기
start = int(input())

#그래프
graph = [[] for _ in range(n)]

#그래프 입력
for i in range(m):
    s,e,w = map(int, input().split())
    graph[s].append((e,w))

# 최단 거리 테이블
distance = [INF] * (n+1)

# 다익스트라
def dijkstra(x):
    q = []
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입(거리, 노드)
    heapq.heappush(q, (0,1))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #거리가 가장 짧은 노드를 선택
        if distance[now] < dist: #기존에 있는 최단 거리보다 길다면, 볼 필요도 없음
            continue
        for i in graph[now]: #현재 노드의 인접 노드들을 모두 반복
            cost = dist + i[1] #비용 = (현재 노드 까지의 최단 거리) + (현재 노드를 거친 인접 노드 까지의 거리)
            if cost < distance[i[0]]: #비용 < 인접 노드의 기존 최단 거리
                distance[i[0]] = cost #최단 거리 갱신
                heapq.heappush(q, (cost, i[0])) #다음 인접 거리를 계산하기 위해 큐에 삽입

dijkstra(start)

for i in range(n+1):
    if distance[i] == INF:
        print("INTFINITY")
    else:
        print(distance[i], end=' ')
