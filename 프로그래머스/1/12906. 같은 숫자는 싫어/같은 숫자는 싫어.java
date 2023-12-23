import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        int[] answer = {};
        
        Stack<Integer> st = new Stack();
        for (int a : arr){
            if (st.isEmpty()){
                st.push(a);
            }
            if(st.peek() == a){
                st.pop();
                st.push(a);
            }
            else {
                st.push(a);
            }
        }
        
        answer = st.stream().mapToInt(Integer::intValue).toArray();

        return answer;
    }
}