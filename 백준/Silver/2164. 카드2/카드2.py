from collections import deque
n=int(input()) #숫자의 개수 입력
queue=deque([i+1 for i in range(n)])
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

for i in queue:
    print(i)