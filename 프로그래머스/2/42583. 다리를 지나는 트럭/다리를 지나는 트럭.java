import java.util.*;

class Solution {
    
    class Truck{
        int weight;
        int move;
        
        public Truck(int weight) {
            this.weight = weight;
            this.move = 1;
        }
        
        public void moving() {
            move++;
        }
    }
    
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Queue<Truck> wait = new LinkedList<>();
        Queue<Truck> move = new LinkedList<>();
        
        for (int w : truck_weights){
            wait.add(new Truck(w));
        }
        
        int answer = 0;
        int curWeight = 0;
        while (!wait.isEmpty() || !move.isEmpty()) {
            answer += 1;
            
            if (move.isEmpty()){
                Truck truck = wait.poll();
                curWeight += truck.weight;
                move.add(truck);
                continue;
            }
            
            for (Truck t : move) {
                t.moving();
            }
            
            if (!wait.isEmpty() && curWeight + wait.peek().weight <= weight) {
                Truck truck = wait.poll();
                curWeight += truck.weight;
                move.add(truck);
            }
            
            if (move.peek().move >= bridge_length) {
                Truck truck = move.poll();
                curWeight -= truck.weight;
            }
        }
        return answer + 1;
    }
}