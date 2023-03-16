import sys
input=sys.stdin.readline
n=int(input())
plan=list(input().split())
x,y=1,1

dx=[-1,1,0,0]
dy=[0,0,-1,1]
move_type=['U','D','L','R']
def func():
    global x
    global y
    for i in plan:
        for j in range(len(move_type)):
            if i == move_type[j]:
                nx=x+dx[j]
                ny=y+dy[j]
                if nx < 1 or ny < 1 or nx > n or ny > n:
                    continue
                x,y=nx,ny
    print(x,y)
func()
