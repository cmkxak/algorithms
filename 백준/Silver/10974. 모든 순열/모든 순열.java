import java.util.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        recursive(new int[n], new boolean[n], 0, 0, n);
        System.out.print(sb);  // 모은 결과를 한 번에 출력
    }

    private static void recursive(int[] arr, boolean[] isVisited, int depth, int idx, int n) {
        if (depth == n) {
            for (int i = 0; i < arr.length; i++) {
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!isVisited[i]) {
                isVisited[i] = true;
                arr[idx] = i + 1;
                recursive(arr, isVisited, depth + 1, idx + 1, n);
                isVisited[i] = false;
            }
        }
    }
}
