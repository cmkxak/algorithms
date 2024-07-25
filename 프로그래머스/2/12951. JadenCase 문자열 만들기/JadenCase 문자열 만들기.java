import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        s = s.toLowerCase();
        String arr[] = s.split(" "); // 빈 문자열을 포함한 배열을 반환하도록 split의 limit 파라미터 사용
        
        for (String str : arr){
            if (!str.isEmpty() && !Character.isDigit(str.charAt(0))) { // 빈 문자열이 아닌 경우 처리
                str = Character.toUpperCase(str.charAt(0)) + str.substring(1);
            }
            answer.append(str).append(" ");
        }
        
        // 마지막 공백 처리
        if (!s.isEmpty() && s.charAt(s.length() - 1) == ' ') {
            return answer.toString();
        }
        
        return answer.toString().trim(); // 마지막 공백 제거
    }
}
