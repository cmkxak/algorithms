import java.io.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().toUpperCase();

        int arr[] = new int[26];

        for (int i = 0; i < s.length(); i++) {
            arr[s.charAt(i) - 65]++;
        }

        int max = Integer.MIN_VALUE;
        char ch = '?';

        for (int i = 0; i < arr.length; i++) {
            if (max < arr[i]) {
                max = arr[i];
                ch = (char) (i + 65);
            } else if (max == arr[i]) {
                ch = '?';
            }
        }
        System.out.println(ch);
    }

}