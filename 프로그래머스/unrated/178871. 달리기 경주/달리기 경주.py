def solution(players, callings):
    pDict = {}
    rDict = {}
    for rank, player in enumerate(players):
        pDict[player] = rank
        rDict[rank] = player
        
    for call in callings:
        nowRank = pDict[call]
        
        pDict[rDict[nowRank]], pDict[rDict[nowRank-1]] = pDict[rDict[nowRank-1]], pDict[rDict[nowRank]]
        rDict[nowRank], rDict[nowRank-1] = rDict[nowRank-1], rDict[nowRank]
        
    return list(rDict.values())
