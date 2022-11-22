#dfs를 활용한 음료수 얼려먹기 문제
#가로, 세로를 공백을 기준으로 입력받음
n,m = map(int, input().split())

#2차원 리스트<2차원 배열>의 맵 정보 입력받기
graph = []
for i in range(n):
  graph.append(list(map(int,input())))

def dfs(x,y):
  #영역에 포함이 안되는 경우, 방문이 불가능한 경우
  if x<=-1 or x>=n or y<=-1 or y>=m:
    return False
  #현재 노드를 아직 방문하지 않았다몀
  if graph[x][y] == 0:
    #해당 노드 방문 처리
    graph[x][y] = 1
    #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출하여 방문 처리
    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)
    return True
  #해당 노드가 이미 방문되어 있다면, False 반환
  return False

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    #현재 위치에서 DFS 수행
    if dfs(i,j) == True:
      result+=1
#정답 출력
print(result)