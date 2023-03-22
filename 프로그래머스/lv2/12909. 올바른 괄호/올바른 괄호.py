def solution(s):
    answer = True
    stack=[]
    
    for i in s:
        if i =='(':
            stack.append(i)
        else:
            if not stack:
                return False
            else:
                stack.pop()
    if len(stack)!=0:
        answer=False
    return answer