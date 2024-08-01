import java.util.*;

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        
        Queue<String> cards1Queue = new LinkedList<>();
        Queue<String> cards2Queue = new LinkedList<>();
        
        for (String s : cards1){
            cards1Queue.add(s);
        }
        
        for(String s : cards2){
            cards2Queue.add(s);
        }
        
        for (int i = 0; i<goal.length; i++){
            String cards1First = cards1Queue.peek();
            String cards2First = cards2Queue.peek();
            
            if (goal[i].equals(cards1First)){
                cards1Queue.poll();
            } else if (goal[i].equals(cards2First)){
                cards2Queue.poll();
            } else {
                answer = "No";
                break;
            }
        }
        
        return answer;
    }
}