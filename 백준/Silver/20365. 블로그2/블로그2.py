n = int(input())
colors = input()

#첫번째 색의 가장 마지막 인덱스를 이용해주어야 한다
cnt = {"B" : 0, "R":0}
cnt[colors[0]] += 1

for i in range(1, n):
    if colors[i] != colors[i-1]:
        cnt[colors[i]] += 1

answer = min(cnt['B'], cnt['R']) + 1
print(answer)