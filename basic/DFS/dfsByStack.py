n,m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    s, e = map(int, input().split())

#인접리스트로 그래프 표현
for i in range(n+1):
    graph[s].append(e)

#방문 리스트
visited = [False] * (n+1)

def dfs(num):
    stack = [num]
    while stack:
        #스택에서 값 삭제
        val = stack.pop()
        print(val, end= ' ')

        for i in graph[val]:
            if not visited[i]:
                visited[num] = True
                stack.append(i)

dfs(1)