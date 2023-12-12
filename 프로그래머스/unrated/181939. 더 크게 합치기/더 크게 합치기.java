class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String cand1 = String.valueOf(a) + b;
        String cand2 = b + String.valueOf(a);
        
        int ans1 = Integer.parseInt(cand1);
        int ans2 = Integer.parseInt(cand2);
        
        
        return ans1 > ans2 ? ans1 : ans2;
    }
}