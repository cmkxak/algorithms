import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) {
        FastScan fastScan = new FastScan();
        HashMap<Character, Integer> wordCountMap = new HashMap<>();

        int max = 0;
        int maxCnt = 0;

        String input = fastScan.next().toUpperCase();

        for (char c : input.toCharArray()) {
            wordCountMap.put(c, wordCountMap.getOrDefault(c, 0) + 1);
        }

        String ans = "";
        for (char c : wordCountMap.keySet()){
            if (wordCountMap.get(c) > max) {
                max = wordCountMap.get(c);
                ans = String.valueOf(c);
            }

        }

        for (int cnt : wordCountMap.values()) {
            if (max == cnt) maxCnt++;
        }

        ans = maxCnt > 1 ? "?" : ans;
        System.out.println(ans);
    }


    static class FastScan {
        BufferedReader br;
        StringTokenizer st;

        public FastScan() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            if (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
    }

}
