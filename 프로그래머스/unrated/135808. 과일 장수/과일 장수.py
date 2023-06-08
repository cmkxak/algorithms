def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    tmp = []
    for i in range(0, len(score),m):
        tmp.append(score[i:i+m])
        
    for i in tmp:
        if len(i) == m:
            answer += i[-1] * m
    
    return answer