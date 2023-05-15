def solution(genres, plays):
    answer,result = [],[]
    totalDict = {}
    
    for i in range(len(genres)):
        answer.append((i, genres[i], plays[i]))
    answer.sort(reverse=True, key = lambda x : (x[1], x[2], -x[0]))
    
    print(answer)
    #장르 구분을 어떤 기준으로 해줘야 할지?
    #리스트를 돌면서 장르별로 전체 재생 횟수를 구해주고, 재생횟수를 기준으로 내림차순 정렬한다.
    
    for val, genre, play in answer:
        totalDict[genre] = totalDict.get(genre, 0) + play
    
    totalList = sorted(totalDict.items(),reverse=True,key=lambda x: x[1])
    print(totalList)
    
    for key,val in totalList:
        cnt = 0
        for val in answer:
            if val[1] == key:
                cnt+=1
                if cnt > 2:
                    break
                else:
                    result.append(val[0])   
    return result