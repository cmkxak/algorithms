import java.util.*;

class Solution {
    private static class State{
        protected int idx;
        protected int value;
        
        public State(int idx, int value){
            this.idx = idx;
            this.value = value;
        }
    }
    
    public int solution(int[] numbers, int target) {
        int answer = 0;
        
        // 초기 상태
        Stack<State> stack = new Stack<>();
        stack.push(new State(0,0));
        
        // 탐색 진행
        while (!stack.isEmpty()){
            //상태 정의
            State state = stack.pop();
            
            //현재 상태 처리 
            if (state.idx == numbers.length){
                if (state.value == target) answer++;
                continue;
            }
            
            // 전이 상태 생성
            stack.push(new State(state.idx + 1, state.value + numbers[state.idx]));
            stack.push(new State(state.idx + 1, state.value - numbers[state.idx]));
        }
        return answer;
    }
}