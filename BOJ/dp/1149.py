#RGB거리
n=int(input())
color=[]
for i in range(n):
    color.append(list(map(int, input().split())))
for i in range(1, n):
    #Red 선택하는 경우
    color[i][0] = min(color[i-1][1], color[i-1][2]) + color[i][0]
    #Blue 선택하는 경우
    color[i][1] = min(color[i-1][0], color[i-1][2]) + color[i][1]
    #Green 선택하는 경우
    color[i][2] = min(color[i-1][0], color[i-1][1]) + color[i][2]
print(color)
print(min(color[n-1][0], color[n-1][1], color[n-1][2]))
