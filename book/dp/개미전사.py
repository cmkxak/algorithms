x=int(input())
foods=list(map(int, input().split()))
print(foods)

dp = [0] * (x+1)

dp[0] = foods[0]
dp[1] = max(foods[0], foods[1])

for i in range(2,x):
    dp[i] = max(dp[i-1], dp[i-2] + foods[i])
print(dp[x-1])