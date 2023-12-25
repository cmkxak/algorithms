import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        ArrayList<String> answer = new ArrayList<>();
        ArrayList<String> arr = new ArrayList<>();
        
        
        for (int i = 0; i<strings.length; i++){
            String c = strings[i].charAt(n) + strings[i];
            arr.add(c);
        }
        
        Collections.sort(arr);
        
        for (int i = 0; i< arr.size() ; i++){
            answer.add(arr.get(i).substring(1));
        }
        
        return answer.toArray(new String[0]);
    }
}