import java.util.*;

class Solution {
    public String solution(String s, int n) {
        StringBuilder sb = new StringBuilder();
        
        char arr[] = s.toCharArray();
        
        for (char c : arr) {
            if (c == ' ') {
                sb.append(' ');
                continue;
            }
            
            if (Character.isLowerCase(c)) {
                if (c + n > 122) {
                    int num = (c + n) - 122 + 97 - 1;
                    sb.append((char)(num));
                } else {
                    char movedCh = (char) (c+n);
                    sb.append(Character.toString(movedCh));
                }
            } else {
                if (c + n > 90) {
                    int num = (c+n) - 90 + 65 - 1;
                    sb.append((char)(num));
                } else {
                    char movedCh = (char)(c+n);
                    sb.append(Character.toString(movedCh));
                }
            }
        }
        return sb.toString();
    }
}