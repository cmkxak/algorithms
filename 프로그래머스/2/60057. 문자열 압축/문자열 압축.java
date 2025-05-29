import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = s.length();
        int n = s.length();
        
        for (int i = 1; i <= n / 2; i++){
            StringBuilder sb = new StringBuilder();
            int prefixCnt = 1;
            String prefix = s.substring(0, i);
            String next = "";
            
            for (int j = i; j < n; j+=i){
                if (j + i > n) {
                    next = s.substring(j, n);    
                } else {
                    next = s.substring(j, j+i);
                }
            
                if (prefix.equals(next)) {
                    prefixCnt++;
                } else {
                    if (prefixCnt > 1) {
                        sb.append(prefixCnt).append(prefix);
                    } else {
                        sb.append(prefix);
                    }
                    prefix = next;
                    prefixCnt = 1;
                }
            }
            if (prefixCnt > 1)
                sb.append(prefixCnt + prefix);
            else
                sb.append(prefix);
            answer = Math.min(answer, sb.toString().length());
        }
        
        return answer;
    }
}