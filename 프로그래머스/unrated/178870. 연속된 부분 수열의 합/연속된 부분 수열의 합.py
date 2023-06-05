def solution(sequence, k):
    answer = []
    
    #구간합 배열 만들기
    prefix = [0]
    sum = 0
    for i in sequence:
        sum += i
        prefix.append(sum)
        
    result = [0, len(prefix)]
    s,e = 0,1
    
    while s < e and e < len(prefix):
        if prefix[e] - prefix[s] == k:
            if e-1 - s < result[1] - result[0]:
                result = [s, e-1]
            e+=1
        elif prefix[e] - prefix[s] < k:
            e+=1
        else:
            s+=1
    return result