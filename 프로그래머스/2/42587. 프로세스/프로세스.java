import java.util.*;

class Solution {        
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();

        for(int i = 0; i < priorities.length; i++){
            queue.add(i);
        }

        while(!queue.isEmpty()){
            int previousSize = queue.size();
            int top = queue.poll();
            
            for (int idx : queue){
                if (priorities[idx] > priorities[top]){
                    queue.add(top);
                    break;
                }
            }
            
            if (queue.size() != previousSize){
                answer++;
                if (top == location) break;
            }
        }
        
        return answer;
    }
}