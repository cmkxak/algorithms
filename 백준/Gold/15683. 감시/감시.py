import copy
n,m=map(int,input().split())
office=[]
cctv=[] # cctv 종류, x좌표, y좌표
#cctv의 모든 방향을 고려해주기 위해서, 각 번호에 맞는 방향 가짓수를 저장해두는 리스트
#결국 dx, dy 리스트의 인덱스를 나타내는 것이고, cctv의 모든 가능한 이동 방향을 찾아내기 위함.
mode=[
    [],
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[0,2],[0,3],[1,2],[1,3]],
    [[0,1,2],[0,1,3],[0,2,3],[1,2,3]],
    [[0,1,2,3]]
]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    data=list(map(int, input().split()))
    office.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j], i,j])
#cctv는 회전할 수 있기 때문에 회전 가능한 모든 경우의 수를 따져 주어서 사각지대를 탐색한다.
def fill(board, num, x, y):
    #CCTV 방향에 따라서
    for i in num:
        #현재 cctv의 위치를 중축으로 이동
        nx=x
        ny=y
        #현재 CCTV를 기준으로 가능할 때 까지 모든 지점을 탐색
        while True:
            nx+=dx[i]
            ny+=dy[i]

            #범위를 벗어나면 중단
            if nx < 0 or ny<0 or nx >= n or ny >= m:
                break

            #벽을 만날 경우 중단
            if board[nx][ny] == 6:
                break

            #그렇지 않은 경우, 감시 가능 지역을 -1로 갱신한다.
            elif board[nx][ny] == 0:
                board[nx][ny] = -1
#재귀적으로 DFS를 사용하여 각 경우에서의 사각지대의 최솟값을 갱신해나간다.
def dfs(depth, office):
    global min_val

    if depth == len(cctv):
        cnt=0

        for i in range(n): #사각 지대 찾기
            cnt+=office[i].count(0)
        min_val=min(min_val, cnt)
        return

    tmp=copy.deepcopy(office)
    #탐색 할 cctv
    cctv_num, x,y = cctv[depth] #4 0 0
    for num in mode[cctv_num]: #CCTV의 방향에 따라서 #[0],[1],[2]
        fill(tmp, num , x, y) # 감시 시작
        dfs(depth+1, tmp) #재귀 호출
        tmp=copy.deepcopy(office) #보드 초기화
min_val=int(1e9)
dfs(0, office)
print(min_val)
