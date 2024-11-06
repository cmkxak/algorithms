import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = new String[strings.length];
        
        changeStrStartsWithNthStr(strings, n);
        Arrays.sort(strings);
        
        for (int i = 0; i<strings.length; i++){
            answer[i] = strings[i].substring(1);
        }
        
        return answer;
    }
    
    public void changeStrStartsWithNthStr(String[] arr, int n){
        for (int i = 0; i<arr.length; i++){
            arr[i] = arr[i].substring(n, n+1) + arr[i];
        }
    }
    
}