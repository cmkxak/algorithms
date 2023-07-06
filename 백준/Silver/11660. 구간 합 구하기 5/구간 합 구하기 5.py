import sys
input = sys.stdin.readline

n,m = map(int, input().split())

nums = [[0] * (n+1)]
prefix = [[0] * (n+1) for i in range(n+1)]
for i in range(n):
    row = [0] + list(map(int, input().split()))
    nums.append(row)

#구간 합 구하기
for i in range(1,n+1):
    for j in range(1,n+1):
        prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + nums[i][j]

for i in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1])