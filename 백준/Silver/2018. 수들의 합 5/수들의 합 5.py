import sys
input = sys.stdin.readline

n = int(input())
s,e = 1,1
sum = 1
cnt = 1
while s<=e and e<n:
    if sum == n:
        e+=1
        sum+=e
        cnt += 1

    elif sum < n:
        e+=1
        sum += e

    elif sum > n:
        sum -= s
        s+=1
print(cnt)