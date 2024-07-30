import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        Queue<Integer> pq = new PriorityQueue<>();
        
        for(int s : scoville){
            pq.add(s);
        }
        
        while (pq.peek() < K){
            if(pq.size() == 1){ //모든 음식의 스코빌 지수가 K 미만인 경우
                return -1;
            }
            pq.add(pq.poll() + pq.poll() * 2);
            answer+=1;
        }
        return answer;
    }
}