import java.util.*;

class Solution {
    public int[] solution(long n) {
        String numStr = Long.toString(n);
        
        int answer[] = new int[numStr.length()];
        
        StringBuilder sb = new StringBuilder(numStr);
        sb.reverse();
        String reversed = sb.toString();
        
        for (int i = 0 ; i < answer.length; i++) {
            char c = reversed.charAt(i);
            answer[i] = Integer.parseInt(Character.toString(c));
        }
        
        return answer;
    }
}