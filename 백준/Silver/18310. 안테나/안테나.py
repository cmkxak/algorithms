import sys
input=sys.stdin.readline
n=int(input())
homes=list(map(int, input().split()))
homes.sort()
idx = (len(homes)-1)//2
print(homes[idx])