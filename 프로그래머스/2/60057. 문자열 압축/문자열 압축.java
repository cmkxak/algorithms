import java.util.*; 

class Solution {    
    public int solution(String s) {
        int answer = s.length(); //최대 길이로 초기화
        
        for (int i = 1; i<=s.length() / 2; i++){    
            StringBuilder sb = new StringBuilder();
            
            String cur = s.substring(0, i);
            int cnt = 1;
            String next = "";
            
            for (int j = i; j< s.length(); j+=i){
                if (j + i > s.length())
                    next = s.substring(j, s.length());
                else
                    next = s.substring(j, j+i);
                if (cur.equals(next)){
                    cnt += 1;
                } else {
                    if (cnt > 1)
                        sb.append(cnt + cur);
                    else
                        sb.append(cur);
                    cur = next;
                    cnt = 1;
                }
            }
            if (cnt > 1)
                sb.append(cnt + cur);
            else
                sb.append(cur);
            answer = Math.min(answer, sb.toString().length());
        }
        return answer;
    }  
}