def solution(name, yearning, photo):
    answer = []
    score = {}
    for i in range(len(name)):
        score[name[i]] = yearning[i]
    
    for info in photo:
        missScore = 0
        for i in info:
            if i in score.keys():
                missScore+= score[i]
        answer.append(missScore)
        
    return answer