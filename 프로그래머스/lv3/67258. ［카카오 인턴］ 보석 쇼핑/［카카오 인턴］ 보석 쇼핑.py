def solution(gems):
    answer = []
    #진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매 
    gems_candidates = set(gems) #모든 종류의 보석
    gems_dict = dict()
    
    for gem in gems_candidates:
        gems_dict[gem] = 0
    check = []
    cnt, start = 0, 0
    for i in range(len(gems)):
        gems_dict[gems[i]] += 1
        
        if gems_dict[gems[i]] >= 1 and gems[i] not in check: 
            cnt+=1
            check.append(gems[i])
            print(check)
        
            if cnt == len(gems_candidates):
                return [start, i+1]
