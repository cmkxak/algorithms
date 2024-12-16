import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int totalCount = nums.length;
        int maxCount = nums.length / 2;
        
        HashSet<Integer> hashSet = new HashSet<>();
        
        for (int n : nums) {
            hashSet.add(n);
        }
        
        if (maxCount < hashSet.size()) //교수님이 주실 수 있는 폰켓몬의 총 수 < 종류의 중복을 제거한 폰켓몬의 수 
            return maxCount;
        
        return hashSet.size();
    }
}