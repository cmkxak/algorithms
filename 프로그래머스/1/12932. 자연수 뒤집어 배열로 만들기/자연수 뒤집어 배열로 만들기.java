class Solution {
    public int[] solution(long n) {
        String str = Long.toString(n);
        String reversed = new StringBuilder(str).reverse().toString();
        char[] c = reversed.toCharArray();
        int[] answer = new int[c.length];
        for(int i = 0; i<c.length; i++){
            answer[i] = c[i] - '0';
        }
        return answer;
    }
}