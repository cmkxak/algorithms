import java.util.*;
import java.io.*;

public class Main {

    private static int[] dy = {-1, 1, 0, 0};
    private static int[] dx = {0, 0, -1, 1};
    private static int N;
    private static int M;
    private static boolean visited[][];

    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        try {
            String[] nums = br.readLine().split(" ");
            N = Integer.parseInt(nums[0]);
            M = Integer.parseInt(nums[1]);
            visited = new boolean[N][M];

            int[][] graph = new int[N][M];

            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                for (int j = 0; j < M; j++) {
                    graph[i][j] = line.charAt(j) - '0';
                }
            }

            bfs(graph, 0, 0);
            System.out.println(graph[N-1][M-1]);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void bfs(int[][] graph, int y, int x) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(y, x));
        visited[y][x] = true;

        while (!queue.isEmpty()) {
            Node current = queue.poll();
            int currentY = current.y;
            int currentX = current.x;

            //현재 좌표로 부터 상,하,좌,우 탐색
            for (int i = 0; i < 4; i++) {
                int ny = currentY + dy[i];
                int nx = currentX + dx[i];

                //범위 벗어나는 경우
                if (ny < 0 || nx < 0 || ny >= N || nx >= M) continue;

                //0 인 경우
                if (graph[ny][nx] == 0) continue;

                if (graph[ny][nx] == 1) {
                    visited[ny][nx] = true;
                    graph[ny][nx] = graph[currentY][currentX] + 1;
                    queue.add(new Node(ny, nx));
                }
            }
        }
    }

    static class Node {
        int y;
        int x;

        public Node(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }
}
