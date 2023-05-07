def solution(array, commands):
    answer = [] 
    for s,e,k in commands:
        new_array = array[s-1:e]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer