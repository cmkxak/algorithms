import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<>();
        ArrayList<Integer> leftDays = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();
        
        //뒤에 있는 기능은 앞에 있는 기능이 배포될 때 함께 배포된다.
        for (int i =0; i < progresses.length; i++){
            int left = (100 - progresses[i]);
            int tmp = 0;
            while (left > 0){
                left-=speeds[i];
                tmp++;
            }
            leftDays.add(tmp);
        }
      
        //2. stack에 넣으면서 앞에 있는 기능이 완성되었는지에 따라 배포 체크
        int lastDay = 0;
        int ans = 0;
        for (int i = 0; i < leftDays.size(); i++){
            if (stack.isEmpty()){
                stack.push(leftDays.get(i));
                continue;
            }
            
            if (stack.peek() < leftDays.get(i)){         
                stack.pop(); //5 10      
                ans++; //1 3                                                                             
                lastDay = leftDays.get(i); //10 20
                stack.push(leftDays.get(i)); //10 20
                answer.add(ans);
                ans = 0;
            } else { 
                ans++; //1 2 1
            }
        }
        
        if (!stack.isEmpty()){
            stack.pop();
            ans++;
            answer.add(ans);
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}