import sys
input = sys.stdin.readline
n,m = map(int, input().split())
pocketmon = dict()
pocketmon2 = dict()
for i in range(1,n+1):
    name = input().rstrip()
    pocketmon[i] = name
    pocketmon2[name] = i

for i in range(m):
    question = input().rstrip()
    if question.isdigit():
        print(pocketmon[int(question)])
    else:
        #문자가 들어온 경우
        print(pocketmon2[question])