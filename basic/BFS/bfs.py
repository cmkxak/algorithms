from collections import deque

def bfs(graph, start, visited):
  # 큐 구현을 위해 deque 라이브러리 사용
  queue = deque([start]) 
  visited[start] = True #현재 노드를 방문 처리
  while queue: # 큐가 빌 때 까지 반복 
    v = queue.popleft() #큐에서 원소 하나를 뽑아 출력
    print(v, end = ' ')
    #해당 원소의 방문하지 않은 인접정점들을 모두 큐에 삽입하고 방문 처리
    for i in graph(v):
      if not visited[i]:
        queue.append(i)
        visited[i] = True

#각 노드가 연결된 정보를 리스트 자료형으로 표현
graph = [
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]
visited = [False] * 9
bfs(graph, 1, visited)