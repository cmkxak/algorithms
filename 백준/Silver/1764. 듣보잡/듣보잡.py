import sys
input = sys.stdin.readline
n,m = map(int, input().split())
no_listen = dict()
answer=[]
for i in range(n):
    name = input().rstrip()
    no_listen[name] = 1
for i in range(m):
    name = input().rstrip()
    if name in no_listen.keys():
        answer.append(name)
print(len(answer))
answer.sort()
for i in answer:
    print(i)