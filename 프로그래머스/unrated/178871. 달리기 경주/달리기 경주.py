def solution(players, callings):
    answer = []
    pDict = {player:rank for rank, player in enumerate(players)}
    rDict = {rank : player for rank,player in enumerate(players)}
    
    for call in callings:
        now = pDict[call] #해설자가 부른 선수의 현재 등수를 가져온다.
        
        pDict[rDict[now]], pDict[rDict[now-1]] = pDict[rDict[now-1]], pDict[rDict[now]]
        rDict[now], rDict[now-1] = rDict[now-1], rDict[now]
    return list(rDict.values())    
    