import java.util.*;
import java.io.*;

public class Main {
    private static boolean[] visited;
    private static int k;
    static List<String> list = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        String[] operators = br.readLine().split(" ");
        visited = new boolean[10];
        
        findVal("", operators, 0);
        
        System.out.println(list.get(list.size() - 1));
        System.out.println(list.get(0));
    }


    private static void findVal(String val, String[] operators, int curIdx) {
        if (curIdx == k + 1) {
            list.add(val);
            return;
        }

        for (int i = 0; i <= 9; i++) {
            if (visited[i]) continue;

            if (curIdx == 0 || isValidOpe(Character.getNumericValue(val.charAt(curIdx - 1)), operators[curIdx - 1], i)) {
                visited[i] = true;
                findVal(val + i, operators, curIdx + 1);
                visited[i] = false;
            }
        }
    }

    private static boolean isValidOpe(int a, String curOper, int b) {
        if (curOper.equals(">")) {
            if (a < b) return false;
        } else if (curOper.equals("<")) {
            if (a > b) return false;
        }
        return true;
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
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }
}
