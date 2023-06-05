def solution(gems):
    #진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매 
    gems_candidates = set(gems) #모든 종류의 보석
    n = len(gems)
    
    check = [1, len(gems)]
    start, end = 0,0
    window = {gems[0]:1} #구간 내의 보석 종류 count
    
    while start < n and end < n:
        if len(window) == len(gems_candidates):
            if end - start < check[1] - check[0]:
                check = [start + 1, end + 1] #3, 7
            else:
                window[gems[start]] -= 1
                if window[gems[start]] == 0:
                    del window[gems[start]]
                start+=1
        else:
            end+=1
            if end == n:
                break
            window[gems[end]] = window.get(gems[end], 0) + 1
    return check
    
    
    #check = []
    #cnt, start = 0, 0
    #for i in range(len(gems)):
        #gems_dict[gems[i]] += 1
        
        #if gems_dict[gems[i]] >= 1 and gems[i] not in check: 
           #cnt+=1
            #check.append(gems[i])
            #print(check)
        
            #if cnt == len(gems_candidates):
                #return [start, i+1]
