import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        ArrayList<Integer> answer = new ArrayList();
        
        answer.add(1);        
        
        for (int i = 2; i<=number; i++){
            int cnt = 0;
            for (int j = 1; j<=Math.sqrt(i); j++){
                if ( i % j == 0){
                    if (Math.pow(j, 2) == i){
                        cnt++;
                    } else {
                        cnt += 2;
                    }
                }
            }

            if (cnt > limit){
                answer.add(power);
            } else {
                answer.add(cnt);
            } 
        }
        return answer.stream().mapToInt(Integer::intValue).sum();
    }
}