import sys
input = sys.stdin.readline
n = int(input())
dx = [-1,1,0,0,-1,-1,1,1] #행
dy = [0,0,-1,1,-1,1,-1,1] #열
def check(x,y):
    cnt = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if bomb[nx][ny] == '*':
            cnt+=1
    return cnt

#지뢰 리스트 입력
bomb = [list(input().rstrip()) for i in range(n)]

#현재 정보
info = [list(input().rstrip()) for i in range(n)]

#결과 리스트
result = [['.'] * (n) for i in range(n)]

def check_bomb():
    for i in range(len(bomb)):
        for j in range(len(bomb[0])):
            if bomb[i][j] == '*':
                result[i][j] = '*'

for i in range(len(info)):
    for j in range(len(info[0])):
        if info[i][j] == 'x' and bomb[i][j] == '*':
            check_bomb()

        if info[i][j] == 'x' and bomb[i][j] =='.':
            answer = check(i, j)
            result[i][j] = str(answer)

for i in result:
    print(''.join(i))