import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> rank = new HashMap();
        
        //현재 등수를 players map에 세팅해준다.
        for (int i = 0; i<players.length; i++){
            rank.put(players[i], i);
        }
        
        for (int i = 0 ; i < callings.length; i++){
            
            //불린 플레이어의 등수
            int callingPlayerRank = rank.get(callings[i]); 
            
            //이전 플레이어 정보 가져오기 
            String frontPlayer = players[callingPlayerRank - 1];
            
            //현재 등수 전광판 갱신 
            rank.put(callings[i], callingPlayerRank - 1); //(불린선수, 현재등수 -1)
            rank.put(frontPlayer, callingPlayerRank); //(불린 선수의 앞의 선수, 현재 등수) 로 한 칸 밀려남
            
            //선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 player 갱신 (현재 순위 갱신)
            players[callingPlayerRank] = frontPlayer;
            players[callingPlayerRank - 1]  = callings[i];
        }
        return players;
    }
}