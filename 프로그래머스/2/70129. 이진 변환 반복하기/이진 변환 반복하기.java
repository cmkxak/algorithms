import java.util.*;

class Solution {
    private static int zeroCnt = 0;
    private static int convertCnt = 0;
    
    public int[] solution(String s) {
        int[] answer = new int[2];
        
        while(true) {
            if ("1".equals(s)) {
                break;
            }            
            
            String str = "";
            int deletedCnt = 0;
            for (int i = 0; i < s.length(); i++){
            
                if (s.charAt(i) == '0') {
                    deletedCnt++;
                } else {
                    str+=s.charAt(i);
                }
            }
            
            s = Integer.toString(str.length(), 2);
            str = "";   
            convertCnt++;
            zeroCnt+=deletedCnt;
        }
        
        answer[0] = convertCnt;
        answer[1] = zeroCnt;
        
        return answer;
    }
}