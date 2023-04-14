import sys
input = sys.stdin.readline

def is_same_color(r,c,size):
  color = data[r][c]
  
  for i in range(r, r+size):
    for j in range(c, c+size):
      if data[i][j] != color:
        return False
  return True

white_cnt, blue_cnt = 0,0

def dfs(r,c,size):
  global white_cnt, blue_cnt
  
  if is_same_color(r,c,size):
    if data[r][c] == 0:
      white_cnt+=1
    else:
      blue_cnt+=1
    return 

  new_size = size//2
  
  dfs(r,c,new_size)
  dfs(r,c+new_size, new_size)

  dfs(r+new_size, c, new_size)
  dfs(r+new_size, c+new_size, new_size)

n = int(input())
data = []
for i in range(n):
  data.append(list(map(int, input().split())))
dfs(0,0,n)
print(white_cnt)
print(blue_cnt)