from collections import deque

def solution(queue1, queue2):
    answer = 0
    sum_q1 = sum_q2 = 0
    
    for i in queue1:
        sum_q1+=i
    for i in queue2:
        sum_q2+=i
    
    target = (sum_q1 + sum_q2) // 2
    
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    while sum_q1 != target:
        if not queue1 or not queue2:
            return -1 
        
        if sum_q1 > target:
            tmp = queue1.popleft()
            sum_q1 -= tmp
            sum_q2+=tmp
            answer += 1
            
        if sum_q2 > target:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_q2 -= tmp
            sum_q1 += tmp
            answer +=1
            
    return answer