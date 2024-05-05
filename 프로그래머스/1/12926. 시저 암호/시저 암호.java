class Solution {
    public String solution(String s, int n){
        String answer = "";
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if(c == ' '){
                answer += c;
            }else if(c >= 'a' && c <= 'z'){
                if(c+n > 'z'){
					answer += (char)(c-26+n);
                }else{
                    answer+= (char) (c + n);           
                }
            }else if(c >= 'A' && c <= 'Z'){
                if(c+n > 'Z'){
                    answer+= (char)(c-26+n);
                }else{
                    answer+= (char) (c + n);   
                }
            }
        }
        return answer;
    }
}