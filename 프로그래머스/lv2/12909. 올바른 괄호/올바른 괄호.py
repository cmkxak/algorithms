def solution(s):
    answer = True
    stack = []
    for i in s:
        if stack and i == ')':
            stack.pop()
            continue
        stack.append(i)
    return len(stack) == 0