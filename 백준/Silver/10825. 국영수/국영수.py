import sys
input=sys.stdin.readline
n = int(input())
classes=[list(input().split()) for _ in range(n)]
for i in sorted(classes, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(i[0])