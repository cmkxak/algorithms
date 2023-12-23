import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answerList = new ArrayList();
        
        for (int a : arr){
            if (a % divisor == 0){
                answerList.add(a);
            }
        }
        int answer[] = answerList.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(answer);
        
        return answer.length > 0 ? answer : new int[]{-1};
    }
}