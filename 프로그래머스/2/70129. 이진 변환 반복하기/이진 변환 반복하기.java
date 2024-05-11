import java.util.*;

class Solution {
    public int[] solution(String s) {
        int cnt = 0;
        int deletedCnt = 0;
        
        while (true){
            if (s.equals("1"))
                break;
            int len = s.length();
            s = s.replaceAll("0", "");
            int changedLen = s.length();
            s = Integer.toString(changedLen, 2);            
            cnt++;
            deletedCnt += (len - changedLen);
        } 
        return new int[]{cnt, deletedCnt};
    }
}