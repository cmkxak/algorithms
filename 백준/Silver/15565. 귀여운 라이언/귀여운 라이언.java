import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    private static int N;
    private static int K;

    public static void main(String[] args) throws IOException {
        ArrayList<Integer> lions = input();
        solve(lions);
    }

    private static void solve(ArrayList<Integer> lions) {
        int result = N;

        if (lions.size() < K) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i <= lions.size() - K; i++) {
            int left = lions.get(i);
            int right = lions.get(i+K - 1);
            result = Math.min(result, right - left + 1);
        }
        System.out.println(result);
    }


    private static ArrayList<Integer> input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> lions = new ArrayList<>();

        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < N; i++) {
            int n = Integer.parseInt(st.nextToken());
            if (n == 1) {
                lions.add(i);
            }
        }
        return lions;
    }
}
