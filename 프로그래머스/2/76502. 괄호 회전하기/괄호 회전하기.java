import java.util.*;

class Solution {
    private static final HashMap<Character, Character> charMap = new HashMap<>();
    
    public int solution(String s) {
        int answer = 0;
        init();
        for (int i = 0; i < s.length(); i++){
            s = s.substring(1) + s.charAt(0);
            if (isValidChar(s)) answer++;
        }
        return answer;
    }
    
    private boolean isValidChar(String s){
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (stack.isEmpty() && isClosed(c)) return false;
            
            if (isOpened(c)){
                stack.push(c);
            } else {
                removeStackEle(c, stack);
            }
        }
        return stack.isEmpty();
    }
    
    private void removeStackEle(char c, Stack<Character> stack){
        if (!stack.isEmpty() && stack.peek() == charMap.get(c)){
            stack.pop();
        }
    }
    
    private boolean isOpened(char c){
        if (c == '[' || c == '{' || c == '(') return true;
        else return false;
    }
    
    private boolean isClosed(char c){
        if (c == ']' || c == '}' || c == ')') return true;
        else return false;
    }
    
    private void init(){
        charMap.put(')', '(');
        charMap.put(']', '[');
        charMap.put('}', '{');
    }
}