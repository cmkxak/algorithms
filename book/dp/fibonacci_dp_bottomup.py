dp = [0] * 100

dp[1]=1
dp[2]=1

#피보나치 함수 - 반복문으로 구현 (Bottom-up, 작은 문제부터 차근차근 값을 구해준다.)
for i in range(3, 100):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[99])