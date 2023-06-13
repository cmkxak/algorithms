t=int(input())

def isRightStr(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            if s[i] == ')':
                return False
            stack.append(s[i])
            continue

        if s[i] == '(':
            stack.append(s[i])

        elif s[i] == ')':
            stack.pop(-1)

    return len(stack) == 0

for i in range(t):
    s = input()
    if isRightStr(s):
        print("YES")
    else:
        print("NO")