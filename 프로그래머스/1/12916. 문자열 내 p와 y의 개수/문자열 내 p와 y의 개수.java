class Solution {
    boolean solution(String s) {
        boolean answer = true;

        
        s = s.toUpperCase();
        
        int cnt = 0;
        for (char c : s.toCharArray()){
            if (c == 'P')
                cnt++;
            else if (c == 'Y')
                cnt--;
        }
        
        return (cnt == 0) ? answer: !answer;
    }
}