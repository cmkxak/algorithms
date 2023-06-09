n, k = map(int, input().split())

#4 1 3 5 2를 역으로 올린다
result = list(map(int, input().split()))
prior = list(map(int, input().split()))

dict_prior = {}
answer = [[0] * n for i in range(k)]
for i, p in enumerate(prior):
    dict_prior[i] = p-1

for i in range(k):
    pos = 0
    while pos < len(result):
        answer[i][dict_prior[pos]] = str(result[pos])
        pos+=1
    result = answer[i]

print(' '.join(answer[-1]))