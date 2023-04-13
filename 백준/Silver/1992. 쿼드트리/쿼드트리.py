#다시 디버깅 과정 눈으로 꼭 보기 ! 진짜 도움이 된다!
def check_color(x,y,size):
    color = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if graph[i][j] != color:
                return False
    return True

answer= ''
def dfs(x,y,size):
    global answer
    if check_color(x,y,size):
        answer+= graph[x][y]
        return
    new_size = size//2

    answer+= '('
    dfs(x,y,new_size) # 2 4 1
    dfs(x, y + new_size, new_size)
    dfs(x+new_size,y,new_size)
    dfs(x+new_size,y+new_size,new_size)
    answer+= ')'

n=int(input())
graph = []
for i in range(n):
    ele = input()
    graph.append(ele)

dfs(0,0,n)
print(answer)