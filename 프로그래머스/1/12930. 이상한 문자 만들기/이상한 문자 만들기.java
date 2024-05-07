import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] arr = s.split(" ", -1);
        StringBuilder sb = new StringBuilder();
        for (int i =0; i<arr.length; i++){
        
            for (int j = 0; j<arr[i].length(); j++){
                char c = arr[i].charAt(j);
            
                if (j % 2 == 0){
                    sb.append(Character.toUpperCase(c));
                } else {
                    sb.append(Character.toLowerCase(c));
                }
            }
            if (i < arr.length - 1){
                sb.append(" ");
            }
        }
        return sb.toString();
    }
}