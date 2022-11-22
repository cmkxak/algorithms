import sys
from collections import deque
input = sys.stdin.readline

# 한번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호 출력
def bfs(x):
    checked = [False] * (n+1)
    count = 0
    # queue 생성
    queue = deque()
    # 시작점 큐에 삽입
    queue.append(x)
    # x로 넘어온 숫자의 방문 체크
    checked[x] = True
    # x의 신뢰 관계 중에
    while queue:
        q = queue.popleft()
        count+=1
        for i in a[q]:
        # 체크하지 않은 신뢰 관계가 있으면
            if not checked[i]:
                checked[i] = True
                queue.append(i)
    return count

#n (컴터 개수) , m (신뢰 관계 수) 입력
n,m = map(int, input().split())

# 컴터들의 신뢰 관계도 그래프 초기화
a = [[] for _ in range(n + 1)]

# 각각의 신뢰 관계 입력
for _ in range(m):
    s,e = map(int, input().split())
    a[e].append(s)

#결과 반환 (가장 많은 컴퓨터를 해킹 -> 가장 많은 정점을 방문하는 정점의 번호 출력)
result = [0 for _ in range(n+1)]

for i in range(1, n+1):
    result[i] = bfs(i)

#해킹 가능한 컴퓨터가 가장 많은 컴퓨터 출력
for i in range(1, n+1):
    if result[i] == max(result):
        print(i, end= ' ')