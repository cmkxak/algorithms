import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        
        HashSet<String> set = new HashSet<>();
        
        for(String num : phone_book){
            set.add(num);   
        }
        
        for(int i=0;i<phone_book.length;i++){
            for(int j =0; j<phone_book[i].length(); j++){
                if (set.contains(phone_book[i].substring(0,j))){
                    System.out.println(phone_book[i].substring(0,j));
                    System.out.println(i);
                    return false;
                }
                }    
            }
        return true;
    }
}