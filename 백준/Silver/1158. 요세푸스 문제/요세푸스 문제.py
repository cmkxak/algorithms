from collections import deque

#원형큐이용문제
n,k = map(int, input().split())
queue = deque(i for i in range(1,n+1))
answer = []
while queue:
    queue.rotate(-(k-1))
    answer.append(queue.popleft())

print('<', end='')
for idx, val in enumerate(answer):
    if idx != n-1:
        print(val, end=', ')
    else:
        print(val, end='')
print('>', end='')