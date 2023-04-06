def solution(N, stages):
    failure = [0] * (N+2)
    tmp,answer = [],[]
    prev_lv_people,result = 0,0
    
    stages.sort()
    
    for i in stages:
        failure[i] +=1
    
    for i in range(1,len(failure)-1):
        prev_lv_people+= failure[i-1]
        
        if failure[i] == 0:
            result = 0
        else:
            result = failure[i] / (len(stages)-prev_lv_people)
            
        tmp.append((i, result))    
    
    tmp.sort(reverse=True,key=lambda x:x[1])
    
    for i,val in tmp:
        answer.append(i)
    return answer