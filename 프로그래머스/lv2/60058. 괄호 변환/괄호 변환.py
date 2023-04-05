def divide_str(p):
    o_count, c_count = 0,0
    
    for i in range(len(p)):
        if p[i] == '(':
            o_count+=1
        else:
            c_count+=1
        
        if o_count == c_count:
            return p[:i+1], p[i+1:] 

#올바른 괄호인지 체크
def is_balanced_str(words):
    stack = []

    for i in words:
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    #과정 1
    if not p:
        return ''
    
    #과정 2
    u,v = divide_str(p)

    #과정 3 :올바른 괄호 문자열이면, 문자열 v에 대해 1단계부터 다시 수행
    if is_balanced_str(u):
        return u + solution(v)
    #과정 4 : 올바른 괄호 문자열이 아니라면
    else:
        new_str= '('
        new_str+= solution(v)
        new_str+= ')'
        for i in u[1:len(u)-1]:
            if i =='(':
                new_str += ')'
            else:
                new_str += '('
        return new_str