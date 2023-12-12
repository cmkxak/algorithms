import java.lang.System;
import java.util.Arrays;
import java.util.*;

class Solution {
    public int[] solution(int[] num_list, int n) {
        ArrayList<Integer> result = new ArrayList<>();
        
        for (int idx =0; idx<num_list.length; idx= idx+n){
            result.add(num_list[idx]);
        }
        
        return result.stream().mapToInt(Integer::intValue).toArray();
    }
}