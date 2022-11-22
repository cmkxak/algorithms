import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int, input().split())
adjacency_n_list = [[] for _ in range(n + 1)]
answer = []
visited = [-1] * (n+1)

#bfs 설계
def bfs(x):
    queue = deque()
    queue.append(x) #시작점 삽입
    visited[x] +=1 #시작점 방문 체크
    while queue: # 큐가 빌 때 까지
        now_node = queue.popleft() #첫번쨰 원소 pop
        for i in adjacency_n_list[now_node]: #pop 한 원소의 인접 정점들중에
            if visited[i] == -1: #방문하지 않은 인접 정점이라면
                visited[i] = visited[now_node] + 1 #방문 체크
                queue.append(i) # 큐에 방문한 정점 삽입

#인접 리스트 생성
for _ in range(m):
    s,e = map(int,input().split())
    adjacency_n_list[s].append(e)

bfs(x)

#거리 정보가 문제에서 주어진 것과 같다면
for i in range(n+1):
    if visited[i] == k:
        answer.append(i) #결과 리스트에 도시 번호 삽입

#거리 정보가 같은 도시가 1개도 존재하지 않으면
if not answer:
    print(-1) #-1 출력

#거리 정보가 같은 도시가 존재한다면
else:
    answer.sort() #도시 번호 정렬
    for i in answer:
        print(i)
