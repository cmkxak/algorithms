t = int(input())
dp = [0] * (101)
p = [1,1,1,2,2,3,4,5,7,9]

for i in range(len(p)):
    dp[i] = p[i]

for i in range(10, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
     n = int(input())
     print(dp[n-1])