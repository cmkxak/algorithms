def solution(arr):
    answer = []
    #원리는 알았으나 코드 표현력이 부족했음
    
    for i in arr:
        if not answer:
            answer.append(i)
        elif answer and answer[-1] == i:
            answer.pop()
            answer.append(i)
        else:
            answer.append(i)
    return answer