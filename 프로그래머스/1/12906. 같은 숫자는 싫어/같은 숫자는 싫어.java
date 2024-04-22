import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        Stack<Integer> stack = new Stack<Integer>();

        for (int i = 0; i < arr.length; i++) {
            if (stack.isEmpty() || stack.peek() != arr[i]) {
                stack.push(arr[i]);
            }
        }

        for (Integer integer : stack) {
            answer.add(integer);
        }

        return answer.stream()
                .mapToInt(Integer::intValue).toArray();
    }
}