import java.util.*;

class Solution {
    public int[] solution(long n) {
        String strValue = Long.toString(n);

        int[] answer = new int[strValue.length()];
        
        for (int i = 0; i < strValue.length(); i++){
            answer[i] = (int) strValue.charAt(strValue.length() - 1 - i) - 48;
        }
        
        
        return answer;
    }
}