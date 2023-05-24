import sys
input = sys.stdin.readline

n = int(input())
greek = [int(input()) for i in range(n)]

greek.sort(reverse=True)
answer = 0

for i in range(0,len(greek)):
    if i % 3 != 2:
        answer += greek[i]
print(answer)