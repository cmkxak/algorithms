import java.util.*;
import java.util.stream.Collectors;


class Solution {
    public int solution(String numbers) {
        Set<Integer> primeSet = new HashSet<>();
        
        int[] nums = numbers.chars()
            .map(c -> c - '0')
            .toArray();
        
        boolean isUsed[] = new boolean[nums.length];
        getPrimes(0, nums, primeSet, isUsed); //현재 숫자, 사용가능한 숫자
        return primeSet.size();
    }
    
    
    //소수 판별 메소드
    public boolean isPrime(int number){
        if (number <= 1) return false;
        
        for (int i = 2; i*i <= number; i ++){
            if (number % i == 0) return false;
        }
        return true;
    }
    
    
    //재귀 메소드
    public void getPrimes(int cur, int[] nums, Set<Integer> primeSet, boolean[] isUsed) {
        if (isPrime(cur)) primeSet.add(cur);
        
        for (int i = 0; i < nums.length; i++){
            if (isUsed[i]) continue; 
            int next = cur * 10 + nums[i];
            isUsed[i] = true;
            getPrimes(next, nums, primeSet, isUsed);
            isUsed[i] = false;
        }
    }
    
}