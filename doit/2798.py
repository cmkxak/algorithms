n,m = map(int, input().split()) #카드의 개수, 최대 수

num = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(i+2, n):
            if num[i] + num[j] + num[k] > m:
                continue
            else:
                result = max(result, num[i]+num[j]+num[k])
print(result)