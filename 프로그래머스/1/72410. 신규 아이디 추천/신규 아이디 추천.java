import java.util.*;

class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        new_id = getNewIdByCondition(new_id);
        new_id = removeFinishMark(new_id);
        new_id = checkFirstAndLastIdx(new_id);
        if (new_id.isEmpty())
            new_id = "a";
        new_id = checkLength(new_id);
        new_id = addLastStr(new_id);
        return new_id;
    }
    
    private String getNewIdByCondition(String str){
        for (char c : str.toCharArray()){
            if (Character.isLowerCase(c) || Character.isDigit(c) || c == '-' || c =='_' || c =='.'){
                continue;
            } else {
                str = str.replace(String.valueOf(c), "");
            }
        }
        return str;
    }
    
    private String removeFinishMark(String str){
        String removed = "";
        String tmp = "";
        
        for (char c : str.toCharArray()){
            if (c == '.'){
                if (!tmp.isEmpty())
                    continue;
                tmp = ".";
            }
            else{
                if (!tmp.isEmpty()){
                    removed += tmp;
                    tmp = "";
                }
                removed += String.valueOf(c);
            }
        }
        return removed.isEmpty() ? tmp : removed;
    }
    
    private String checkFirstAndLastIdx(String str){
        if (str.startsWith(".")){
            str = str.substring(1);
        } else if (str.endsWith(".")){
            str = str.substring(0, str.length()-1);
        }
        return str;
    }
    
    private String checkLength(String str){
        if (str.length() >= 16){
            str = str.substring(0, 15);
        }
        
        if (str.endsWith(".")){
            str = str.substring(0, 14);
        }
        return str;
    }
    
    private String addLastStr(String str){
        String last = String.valueOf(str.charAt(str.length()-1));
        if (str.length() <= 2) {
            while (str.length() <= 2){
                str += last;
            }
        }
        return str;
    }    
}