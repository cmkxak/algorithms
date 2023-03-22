def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0:
            answer.append(i)
            
        elif answer[-1] == i:
            answer.pop()
            answer.append(i)
        else:
            answer.append(i)
    return answer
