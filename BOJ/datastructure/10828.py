import sys
input = sys.stdin.readline
stack_list = []
count = 0

def push(x):
    stack_list.append(x)

def isEmpty():
    print(1) if not stack_list else print(0)

def pop():
    if not stack_list:
        print(-1)
    else:
        print(stack_list.pop())

def size():
    print(len(stack_list))

def top():
    if not stack_list:
        print(-1)
    else:
        print(stack_list[-1])

n = int(input())
for i in range(n):
    ord = input().split()
    if ord[0] == "push":
        push(ord[1])
    elif ord[0] == "pop":
        pop()
    elif ord[0] == "empty":
        isEmpty()
    elif ord[0] == "top":
        top()
    elif ord[0] == "size":
        size()
