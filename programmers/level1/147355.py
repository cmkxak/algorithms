def solution(t, p):
    answer = 0
    s=0
    e=len(p)

    while e<=len(t):
        tmp=t[s:e]
        if int(tmp) <= int(p):
            answer+=1
            s+=1
            e+=1
        else:
            s+=1
            e+=1

    return answer