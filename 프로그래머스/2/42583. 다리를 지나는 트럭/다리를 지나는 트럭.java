import java.util.*;


class Solution {
   public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int sum = 0;
        
        Queue<Integer> queue = new LinkedList();
        
        for (int i = 0; i < truck_weights.length; i++){
            int truckWeight = truck_weights[i];
            
            while(true) {
                
                //큐가 비어있는 경우 
                if (queue.isEmpty()){ 
                    answer+=1;
                    sum += truckWeight;
                    queue.add(truckWeight);
                    break;
                    
                //큐가 가득찬 경우 
                } else if (queue.size () == bridge_length){
                    sum-=queue.poll();
                
                //큐에 원소를 추가할 수 있는 경우
                } else {
                    if (truckWeight + sum <= weight){
                        queue.add(truckWeight);
                        sum+= truckWeight;
                        answer += 1;
                        break;
                } else {
                        //!!! 핵심 : 무게가 넘는 경우 0을 넣어 기존의 존재하는 트럭이 강을 건너게 한다 //
                        queue.offer(0);
                        answer += 1;
                    }
                }
            }
        }
        return answer + bridge_length;
    }
}