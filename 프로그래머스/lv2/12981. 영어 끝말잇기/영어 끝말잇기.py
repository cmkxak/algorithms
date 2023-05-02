def solution(n, words):
    answer = []
    level = []
    for i in range(0,len(words),n):
        level.append(words[i:n + i])
    print(level)
    #탈락 조건
    #이전 단어의 마지막 != 다음 시작 단어
    
    for idx, l in enumerate(level):
        for j in range(1,len(l)): 
            if level[j-1][-1] != level[j][0]:
                answer.append(j)
                answer.append(idx)
    print(answer)
    
    
    return answer