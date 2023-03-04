#나머지 합 구하기
n,m=map(int,input().split())
nums=list(map(int,input().split()))
print(nums)
s=[0] *(n+1)
print(s)
for i in range(1,n+1):
    #구간 합 구하기
    s[i]=s[i-1]+nums[i-1]
print(s)

# 나머지 구하는 로직 추가해주어야 함
# for i in range(n):
#     for j in range(i+1,n):
#         if s[]