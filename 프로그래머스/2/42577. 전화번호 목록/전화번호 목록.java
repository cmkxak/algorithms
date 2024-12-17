import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        
        HashSet<String> set = new HashSet<>();
        
        for (String phoneNum : phone_book){
            set.add(phoneNum);
        }
        
        for (int i =0; i< phone_book.length;i++){
            for (int j = 0; j < phone_book[i].length(); j++) {
                String curPrefix = phone_book[i].substring(0, j);
                if (set.contains(curPrefix)) return false;
            }
        }
        
        return answer;
    }
}