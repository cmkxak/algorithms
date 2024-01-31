import java.io.*;
import java.util.*;

public class Main {

    static StringTokenizer st;
    static BufferedReader br;
    private static int S, N;
    private static int A[];

    public static void input() throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());
        A = new int[N + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
    }

    static void solve() {
        int ans = N + 1;
        int R = 0;
        int sum = 0;

        for (int L = 1; L <= N; L++) {
            sum -= A[L - 1];

            while (R + 1 <= N && sum < S) {
                R++;
                sum += A[R];
            }

            if (sum >= S) {
                ans = Math.min(ans, R - L + 1);
            }
        }
        if (ans == N + 1) {
            ans = 0;
        }
        System.out.println(ans);
    }

    public static void main(String[] args) throws IOException {
        input();
        solve();
    }
}
