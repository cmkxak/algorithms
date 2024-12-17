import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    private static final int END_NUMBER = 0;

    public static void main(String[] args) {

        FastScan fastScan = new FastScan();

        while (true) {
            int a = Integer.parseInt(fastScan.next());
            int b = Integer.parseInt(fastScan.next());
            int c = Integer.parseInt(fastScan.next());

            if (a == END_NUMBER && b == END_NUMBER && c == END_NUMBER)
                break;

            printTriangleInfo(a, b, c);
        }

    }

    private static void printTriangleInfo(int a, int b, int c) {
        //가장 긴변의 길이 < 나머지 두 변의 길이의 합
        int tempMax = Math.max(a, b);
        int realMax = Math.max(tempMax, c);

        if (isNotValidTriangle(realMax, a, b, c))
            return;

        if (a == b && b == c) {
            System.out.println("Equilateral");
            return;
        }

        //세변의 길이가 모두 다른 경우
        if (a != b && b != c && a != c) {
            System.out.println("Scalene");
            return;
        }

        //두변의 길이만 같은 경우
        if ((a == b && c != b) || (b == c && c != a) || (a == c && c != b)) {
            System.out.println("Isosceles");
            return;
        }
    }

    private static boolean isNotValidTriangle(int max, int a, int b, int c) {
        int sumOfTwoLine = 0;

        if (max == a) {
            sumOfTwoLine = b + c;
        }

        if (max == b) {
            sumOfTwoLine = a + c;
        }

        if (max == c) {
            sumOfTwoLine = a + b;
        }

        if (max >= sumOfTwoLine) {
            System.out.println("Invalid");
            return true;
        }
        return false;
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
