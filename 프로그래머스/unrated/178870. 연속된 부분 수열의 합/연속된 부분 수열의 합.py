def solution(sequence, k):
    #1. 구간합을 구해준다.
    prefix = [0]
    sum = 0
    for i in sequence:
        sum+=i
        prefix.append(sum)
    result = [0,len(sequence)]
    s,e = 0,1
    
    while s<e and e < len(prefix):
        if prefix[e] - prefix[s] == k:
            if e-1-s < result[1] - result[0]:
                result = [s, e-1]
            e+=1
        elif prefix[e] - prefix[s] > k:
            s+=1
        else:
            e+=1
    
    return result