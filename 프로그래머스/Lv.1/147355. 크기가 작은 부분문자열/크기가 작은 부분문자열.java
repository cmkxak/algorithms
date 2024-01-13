class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        
        long compVal = Long.parseLong(p);
        
        for (int i = 0; i< t.length() - p.length() + 1; i++){
            String substr = t.substring(i, i + p.length());
            if (compVal >= Long.parseLong(substr)){
                answer++;
            }
        }
        return answer;
    }
}