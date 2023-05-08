def solution(people, limit):
    answer = 0
    
    people.sort()
    
    s,e = 0, len(people) - 1
    
    while s<=e:
        answer+=1
        if people[s] + people[e] > limit:
            e-=1
        else:
            #무게가 초과하지 않으므로 두명을 태웠다고 가정하면, 시작점과 끝점에 위치한 사람 제거
            s+=1
            e-=1
    return answer