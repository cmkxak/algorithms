from collections import deque
import sys
input= sys.stdin.readline

def push(ele):
    queue.append(ele)
def pop():
    if not queue:
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if not queue:
        print(1)
    else:
        print(0)

def front():
    if not queue:
        print(-1)
    else:
        print(queue[0])

def back():
    if not queue:
        print(-1)
    else:
        print(queue[-1])

queue = deque()
t = int(input())
for i in range(t):
    s = input().split()

    if s[0] == 'push':
        push(int(s[1]))
    elif s[0] == 'pop':
        pop()
    elif s[0] == 'size':
        size()
    elif s[0] == 'empty':
        empty()
    elif s[0] == 'front':
        front()
    elif s[0] == 'back':
        back()