import java.util.*;

class Solution {
    private static List<String> words = new ArrayList<>();
    private static String[] candidates = {"A", "E", "I", "O", "U"};
        
    public int solution(String word) {
        
        recursive("");
        
        for (int i = 0; i < words.size(); i++){
            if (words.get(i).equals(word)) return i;
        }
        
        return 0;
        
    }
    
    private void recursive(String cur){
        words.add(cur);
        
        if (cur.length() == 5) return;
        
        for (int i = 0; i < candidates.length; i++){
            recursive(cur + candidates[i]);
        }
        
        
    }
}