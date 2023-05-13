stringDict = {"(":0, ")":0,
             "[":1,"]":1,
              "{":2, "}":2
             }
def isRightString(s):
    stack = []
    for i in s:
        if i in ["(" , "[", "{"]:
            stack.append(stringDict[i])
        else:
            if not stack:
                return False
            
            if stack and stack.pop() != stringDict[i]:
                return False
    return not stack
    
def solution(s):
    answer = 0

    for i in range(len(s)):
        curvedS = s[i:] + s[:i]
        if isRightString(curvedS):
            answer+=1
        
    return answer