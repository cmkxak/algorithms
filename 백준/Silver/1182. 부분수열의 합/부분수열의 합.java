import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int N, S;
    static int[] nums;
    static int cnt;

    public static void recursive(int k, int value) {
        if (k == N + 1) {
            if (value == S) cnt++;
        } else {
            recursive(k + 1, value + nums[k]);
            recursive(k + 1, value);
        }
    }

    public static void main(String[] args) throws Exception {
        input();
        recursive(1, 0);
        if (S == 0) {
            cnt--;
        }
        System.out.println(cnt);

    }


    public static void input() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        S = Integer.parseInt(st.nextToken());

        nums = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());

        }
    }

}
