import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(arr[0]);
        
        for (int i = 1; i< arr.length; i++){
            if (arr[i] != list.get(list.size()-1))
                list.add(arr[i]);
        }
        
        return list.stream().mapToInt(Integer::intValue).toArray();
    }
}