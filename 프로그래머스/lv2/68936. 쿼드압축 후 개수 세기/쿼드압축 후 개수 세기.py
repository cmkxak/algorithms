def is_same(arr,x,y,size):
    number = arr[x][y]
    for i in range(x, size+x):
        for j in range(y, size+y):
            if number != arr[i][j]:
                return False
    return True

zero_cnt, one_cnt = 0,0

def dfs(x,y,size,arr):
    global zero_cnt, one_cnt
    
    if is_same(arr,x,y,size):
        if arr[x][y] == 1:
            one_cnt+=1
        else:
            zero_cnt+=1
        return
    
    size = size // 2
        
    dfs(x,y,size,arr)
        
    dfs(x,y + size,size,arr)
        
    dfs(x+size,y,size,arr)
        
    dfs(x+size, y+size, size, arr)
    
def solution(arr):
    answer = []
    dfs(0,0,len(arr),arr)
    answer.append(zero_cnt)
    answer.append(one_cnt)
    return answer