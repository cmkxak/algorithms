import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        FastScan fastScan = new FastScan();
        int N = Integer.parseInt(fastScan.next());

        HashMap<Integer, Integer> numbers = new HashMap<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(fastScan.next());
            numbers.put(num, numbers.getOrDefault(num, 0) + 1);
        }

        int M = Integer.parseInt(fastScan.next());
        for (int i = 0; i < M; i++) {
            int num = Integer.parseInt(fastScan.next());
            sb.append(numbers.getOrDefault(num, 0))
                    .append(' ');
        }
        System.out.println(sb.toString());
    }


    static class FastScan {
        BufferedReader br;
        StringTokenizer st;

        public FastScan() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
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
