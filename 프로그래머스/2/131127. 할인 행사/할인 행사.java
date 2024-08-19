import java.util.*;

class Solution {
    private static final HashMap<String, Integer> orderBucket = new HashMap<>();
    
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        for (int i = 0; i < want.length; i++){
            orderBucket.put(want[i], number[i]);
        }
        
        for (int i = 0; i< discount.length - 10 + 1; i++){
            HashMap<String, Integer> marketInfo = new HashMap<>();
            
            for (int j = i; j < i + 10; j++){
                Integer discountCnt = marketInfo.getOrDefault(discount[j], 0) + 1;
                marketInfo.put(discount[j], discountCnt);
            }
            
            Boolean isIdentical = true;
            
            for(String key : orderBucket.keySet()){
                if(orderBucket.get(key) != marketInfo.get(key)){
                    isIdentical = false;
                    break;
                }
            }
            
            answer += isIdentical ? 1 : 0;
        }
        
        return answer;
    }
        
}