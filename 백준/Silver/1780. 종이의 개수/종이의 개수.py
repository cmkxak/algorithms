def check_color(row, col, size):
    color = papers[row][col] # 6 0 
    for x in range(row, row+size): #6 - 8
        for y in range(col, col+size): # 0 - 2
            if papers[x][y] != color:
                return False
    return True

def partition(row, col, size):
    global minus_one, zero, one
    #같은 색상인 경우
    if check_color(row,col,size):
        if papers[row][col] == -1:
            minus_one+=1
        elif papers[row][col] == 0:
            zero +=1
        else:
            one+=1
        return

    new_size = size // 3

    partition(row, col, new_size) #왼쪽 위 6 0
    partition(row, col + new_size, new_size) #중앙 위 6 1
    partition(row, col + 2 * new_size, new_size) #중앙 오른쪽 6 2

    partition(row + new_size, col, new_size) #왼쪽 중간 # 7 0
    partition(row + new_size, col+ new_size, new_size) #중앙 중간 # 7 1
    partition(row + new_size, col+ 2 * new_size, new_size) #오른쪽 중간 # 7 2

    partition(row + 2 * new_size, col, new_size) #왼쪽 아래 6 2
    partition(row + 2 * new_size, col+ new_size, new_size) #중앙 아래 6 1
    partition(row + + 2 * new_size, col+ 2 * new_size, new_size) #오른쪽 아래 6 2 

n = int(input())
papers = []
for i in range(n):
    papers.append(list(map(int, input().split())))
minus_one, zero, one = 0,0,0
partition(0,0,n)
print(f'{minus_one}\n{zero}\n{one}')