import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        String result = "";

        for (int i = 0; i < a.length(); i++) {
            int ascNum = (int) a.charAt(i);

            if (ascNum >= 65 && ascNum <= 90) {
                ascNum = ascNum + 32;
            } else if (ascNum >= 97 && ascNum <= 122) {
                ascNum = ascNum - 32;
            }
            result += (char) ascNum;
        }

        System.out.print(result);
    }
}