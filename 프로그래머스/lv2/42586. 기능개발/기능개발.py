import math
def solution(progresses, speeds):
    answer = []
    completion = []
    
    for i in range(len(progresses)):
        completion.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    front = 0
    print(completion)
    for i in range(len(completion)):
        if completion[i] > completion[front]:
            print(i, front)
            answer.append(i-front)
            front = i
    answer.append(len(completion) - front)
    
    return answer