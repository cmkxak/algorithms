from collections import deque

def change_l(n):
    front = n % 1000
    back = n // 1000
    res = front * 10 + back
    return res

def change_r(n):
    front = n%10
    back = n//10
    res = front * 1000 + back
    return res

def change_d(n):
    n = 2*n
    if n > 9999:
        res = n % 10000
    else:
        res = n
    return res

def change_s(n):
    if n == 0:
        return 9999
    else:
        return n-1

def bfs(n, target):
    queue = deque()
    visited = [0] * (10001)
    visited[n] = 1
    operate = ""
    queue.append((n, operate))

    while queue:
        cur_num,ope = queue.popleft()

        if cur_num == target:
            print(ope)
            return

        tmp = change_l(cur_num)
        if not visited[tmp]:
            visited[tmp] = 1
            queue.append((tmp, ope + "L"))

        tmp = change_r(cur_num)
        if not visited[tmp]:
            visited[tmp] = 1
            queue.append((tmp, ope + "R"))

        tmp = change_d(cur_num)
        if not visited[tmp]:
            visited[tmp] = 1
            queue.append((tmp, ope + "D"))

        tmp = change_s(cur_num)
        if not visited[tmp]:
            visited[tmp] = 1
            queue.append((tmp, ope+ "S"))

t = int(input())
for i in range(t):
    a,b = map(int, input().split())
    bfs(a,b)