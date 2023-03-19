def solution(array, commands):
    answer=[]
    for val in commands:
        i=val[0]-1
        j=val[1]
        k=val[2]-1
        answer.append(sorted(array[i:j])[k])
    
    return answer