import java.util.*;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int answer = 0;
        int arrayA_gcd = getArrGCD(arrayA); //1
        int arrayB_gcd = getArrGCD(arrayB); //2
        
        if (arrayA_gcd != 0) 
            if (!isDivided(arrayA_gcd, arrayB)) answer = Math.max(answer, arrayA_gcd);
        if (arrayB_gcd != 0)
            if (!isDivided(arrayB_gcd, arrayA)) answer = Math.max(answer, arrayB_gcd);
        
        return answer;
    }
        
    //최대 공약수를 리턴하는 메소드
    public int gcd(int a, int b){
        if (a % b == 0) return b;
        return gcd(b, a % b); 
    }
    
    public int getArrGCD(int[] arr){
        if (arr.length == 1) return arr[0];
        
        int arrGCD = gcd(arr[0], arr[1]);
        
        if (arr.length > 2) {
            for (int i = 2; i < arr.length; i++) 
                arrGCD = gcd(arrGCD, arr[i]);
        }
        return arrGCD;
    }
    
    public boolean isDivided(int n, int[] arr){
        for (int i = 0; i < arr.length; i++){
            if (arr[i] % n == 0) return true;
        }
        return false;
    }
    
}