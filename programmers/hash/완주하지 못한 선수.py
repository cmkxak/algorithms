def solution(participant, completion):
    answer = ''
    dict_p = dict()

    for i in participant:
        if i not in dict_p:
            dict_p[i] = 1
        else:
            dict_p[i]+=1

    for i in completion:
        if dict_p[i] == 1:
            dict_p[i] = 0
        else:
            dict_p[i]-=1

    for k in dict_p.keys():
        # 완주하지 못한 선수는 어차피 1명 by 문제 조건
        if dict_p.get(k) == 1:
            answer = k
    return answer