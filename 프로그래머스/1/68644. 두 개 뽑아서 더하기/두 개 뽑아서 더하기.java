import java.util.*;

class Solution {
    
    private static List<Integer> answer = new ArrayList<>();
    
    public int[] solution(int[] numbers) {
        
        for (int i = 0; i < numbers.length; i++) {
            int a = numbers[i];
            for (int j = i+1; j < numbers.length; j++) {
                int b = numbers[j];
                if (!answer.contains(a+b))
                    answer.add(a + b);
            }
        }
        
        Collections.sort(answer);
        
        //중복 제거 how ? 
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}