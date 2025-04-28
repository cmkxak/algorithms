import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int scores[]  = new int[n];

        for (int i = 0; i < n; i++) {
            scores[i] = sc.nextInt();
        }

        int max = Integer.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            max = Math.max(max, scores[i]);
        }

        double fakeTotalScore = 0;

        for (int i = 0; i < n; i++) {
            fakeTotalScore += (double) scores[i] / max * 100;
        }

        System.out.println(fakeTotalScore / n);
    }
}
