import sys
input = sys.stdin.readline
n,m = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0]
sum = 0
#구간합 구하기
for i in nums:
    sum += i
    prefix.append(sum)
for i in range(m):
    s,e = map(int,input().split())
    print(prefix[e] - prefix[s-1])