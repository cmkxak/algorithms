import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        answer = getMaxDefenceRound(n, k, pq, enemy);
        
        return answer;
    }
    
    private int getMaxDefenceRound(int n, int k, PriorityQueue<Integer> pq, int[] enemies){
        int cnt = 0;

        //1. pq에 무조건 넣기.
        for(int i = 0; i< enemies.length; i++){
            if (k > 0){
                pq.add(enemies[i]);
                k--;
            } else {
                //무적권을 다 쓴 경우 
                // 우선순위 큐의 첫번째 원소 < 적의 수 
                if (!pq.isEmpty() && pq.peek() < enemies[i]){
                    n -= pq.poll();
                    pq.add(enemies[i]);
                } else { // 우선순위 큐의 첫번째 원소 >= 적의 수 
                    n -= enemies[i];
                }
            }
            if (n < 0) break;
            cnt++;
        }
        return cnt;
    }
}