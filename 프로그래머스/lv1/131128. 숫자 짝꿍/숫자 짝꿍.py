def solution(X, Y):
    answer = ''
    max = 0
    for i in range(9,-1,-1):
        cnt = min(X.count(str(i)), Y.count(str(i))) 
        answer += str(i) * cnt
    
    if not answer:
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer