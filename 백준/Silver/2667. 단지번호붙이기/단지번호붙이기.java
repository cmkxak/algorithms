import java.io.*;
import java.util.*;

public class Main {

    static int[][] graph;
    static boolean[][] visited;
    static int answer = 0;
    static ArrayList<Integer> answerList;

    static int homeCnt = 1;
    static final int[] dx = {-1, 1, 0, 0};
    static final int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) {
        FastScan scan = new FastScan();
        int size = scan.nextInt();

        graph = new int[size][size];
        visited = new boolean[size][size];
        answerList = new ArrayList<>();

        for (int i = 0; i < size; i++) {
            String row = scan.next();
            for (int j = 0; j < size; j++) {
                graph[i][j] = Integer.parseInt(row.substring(j, j + 1));
            }
        }

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (graph[i][j] != 0) {
                    if (!visited[i][j]) {
                        visited[i][j] = true;
                        answer++;
                        dfs(graph, visited, i, j);
                        answerList.add(homeCnt);
                        homeCnt = 1;
                    }
                }
            }
        }
        Collections.sort(answerList);
        System.out.println(answer);
        for (int i = 0; i < answerList.size(); i++) {
            System.out.println(answerList.get(i));
        }
    }

    public static void dfs(int[][] graph, boolean[][] visited, int x, int y) {
        int nx = x;
        int ny = y;

        for (int i = 0; i < 4; i++) {
            nx = x + dx[i];
            ny = y + dy[i];

            if (nx >= 0 && nx < graph.length && ny >= 0 && ny < graph.length) {
                if (graph[nx][ny] != 0) {
                    if (!visited[nx][ny]) {
                        visited[nx][ny] = true;
                        homeCnt++;
                        dfs(graph, visited, nx, ny);
                    }
                }
            }
        }
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
