import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수 입력받기
n,m = map(int, input().split())
#시작 노드 번호 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
#방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    #시작 노드에서 종료 노드로 가는 비용이 w라는 의미
    s,e,w = map(int, input().split())
    graph[s].append((e,w))

#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index #최단 거리가 가장 짧은 노드 반환

def dijkstra(start):
    # 시작 노드 초기화
    distance[start] = 0

    # 시작 노드 방문 처리
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    # 방문 하지 않은 노드 중, 가장 최단 거리가 짧은 노드의 번호를 반환
    for j in range(n-1):
        #현재 최단 거리가 가장 짧은 노드르 꺼내서, 방문 처리
        now_node = get_smallest_node()
        visited[now_node] = True
        # 그 노드의 인접 노드를 방문하여, 최단 경로 계산
        for k in graph[now_node]:
            cost = distance[now_node] + k[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 최단 경로 갱신
        if cost < distance[k[0]]:
            distance[k[0]] = cost

#다익스트라 알고리즘 수행
dijkstra(start)

#최단 경로 리스트 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i], end=' ')