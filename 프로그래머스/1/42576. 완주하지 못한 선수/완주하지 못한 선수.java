import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> playerInfo = new HashMap<>();
        
        //참가자 초기화
        for (String p : participant) {
            playerInfo.put(p, playerInfo.getOrDefault(p, 0) + 1);    
        }
        
        //참가자 중 완주자의 수는 차감한다.
        for (String c : completion) {
            playerInfo.put(c, playerInfo.get(c) - 1); 
        }
        
        for (String name : playerInfo.keySet()){
            if (playerInfo.get(name) != 0)
                return name;
        }
        
        return answer;
    }
}