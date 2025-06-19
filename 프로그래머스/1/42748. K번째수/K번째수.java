import java.util.*;

class Solution {
    private static List<Integer> answer = new ArrayList<>();
    
    public int[] solution(int[] array, int[][] commands) {
        
        for (int[] command : commands) {
            int start = command[0];
            int end = command[1];
            int k = command[2];
            int size = end - start + 1;
            
            int[] nums = new int[size];
            
            int idx = 0;
            
            for (int i = start - 1; i < end; i++) {
                nums[idx++] = array[i];
            }
            
            Arrays.sort(nums);
            answer.add(nums[k-1]);
        }
        
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}