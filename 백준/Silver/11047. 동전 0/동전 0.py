n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
answer = 0
for coin in coins:
    if k == 0:
        break
    answer += (k // coin)
    k = k % coin
print(answer)