n,m=map(int, input().split())
nums=[[0] * (n+1)]
#표에 채워져 있는 수
for i in range(n):
    temp=[0]+list(map(int, input().split()))
    nums.append(temp)
#합 배열 구해주어야 함.
s=[[0] * (n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + nums[i][j] #배열 합 구하기
for j in range(m):
    s1,e1,s2,e2=map(int,input().split())
    ans=s[s2][e2]-s[s2][e1-1]-s[s1-1][e2]+s[s1-1][e1-1] # 3 4 - 3 3
    print(ans)