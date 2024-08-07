import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static List<Integer>[] list;
    private static boolean visited[];
    private static int answer = -1;

    public static void main(String[] args) throws IOException {
        FastScan fastScan = new FastScan();
        int n = fastScan.nextInt();

        list = new ArrayList[n + 1];
        visited = new boolean[n + 1];

        int end = fastScan.nextInt();
        int start = fastScan.nextInt();

        int m = fastScan.nextInt(); //부모 - 자식간의 관계

        for (int i = 1; i <= n; i++) {
            list[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            int node = fastScan.nextInt();
            int adj = fastScan.nextInt();
            list[node].add(adj);
            list[adj].add(node);
        }

        dfs(list, start, end, visited, 0);
        System.out.println(answer);
    }

    public static void dfs(List<Integer>[] list, int curNode, int end, boolean[] visited, int cnt) {
        visited[curNode] = true;

        for (int i = 0; i < list[curNode].size(); i++) {
            int adjacentNode = list[curNode].get(i);
            if (!visited[adjacentNode]) {
                if (adjacentNode == end) {
                    answer = cnt + 1;
                    return;
                }
                dfs(list, adjacentNode, end, visited, cnt + 1);
            }
        }
    }


    static class FastScan {
        BufferedReader br;
        StringTokenizer st;

        public FastScan() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() throws IOException {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() throws IOException {
            return Integer.parseInt(next());
        }

    }
}
