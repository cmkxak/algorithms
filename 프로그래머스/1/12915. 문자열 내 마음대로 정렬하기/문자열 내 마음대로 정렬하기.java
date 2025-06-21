import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        int idx = 0;
        for (String s : strings){
            strings[idx++] = s.charAt(n) + s; 
        }
        
        Arrays.sort(strings);
        
        for (int i = 0; i < strings.length; i++){
            answer[i] = strings[i].substring(1);
        }
        
        return answer;
    }
}