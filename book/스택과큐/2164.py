from collections import deque
import sys
input=sys.stdin.readline
n=int(input()) #숫자의 개수 입력
queue=deque([i+1 for i in range(n)])

#queue의 크기가 1이 될 때 까지 아래 로직을 반복한 뒤 큐에 남은 원소를 출력한다.
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])