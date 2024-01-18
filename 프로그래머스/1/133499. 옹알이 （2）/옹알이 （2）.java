import java.util.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        for (String b : babbling){
            String tmp1 = b.replace("ayaaya","1").replace("yeye","2").replace("woowoo","3").replace("mama","4");
            
            String tmp2 = tmp1.replace("aya"," ").replace("ye"," ").replace("woo"," ").replace("ma"," ");
            String tmp3 = tmp2.replace(" ", "");
            
            if (tmp3.length() == 0) answer++;
        }
        
        return answer;
    }
}