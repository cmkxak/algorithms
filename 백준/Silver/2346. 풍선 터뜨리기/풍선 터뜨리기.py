from collections import deque

n = int(input())
queue = deque(enumerate(map(int, input().split())))
answer = []
while queue:
    idx, val = queue.popleft()
    answer.append(idx + 1)

    #양수라면 오른쪽으로 이동 - deque의 rotate() 사용
    if val > 0:
        queue.rotate(-(val-1))
    #음수라면 왼쪽으로 이동
    else:
        queue.rotate(-val)
    #print(queue)
print(*answer)