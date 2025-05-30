import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        
        int cnt = 0;
        s = s.toLowerCase();
        for (char c : s.toCharArray()) {
            if (c == 'p') 
                cnt++;
            else if (c == 'y')
                cnt--;
        }        

        return (cnt == 0) ? answer : !answer;
    }
}