def solution(players, callings):
    ranking = {}
    for idx, player in enumerate(players):
        ranking[player] = idx
    
    for calledPlayer in callings:
        #앞지른 선수 index
        called_player_idx = ranking[calledPlayer]
        
        #뒤쳐진 선수의 이름
        front_player = players[called_player_idx -1]
        
        #랭킹 정보 변경
        ranking[calledPlayer] = called_player_idx - 1
        ranking[front_player] = called_player_idx
        
        players[called_player_idx] = front_player
        players[called_player_idx-1] = calledPlayer
    return players