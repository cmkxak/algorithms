/**
 * 유기농배추
 */
import java.util.*;
import java.io.*;

public class Main {

    private static int dy[] = {-1, 1, 0, 0}; //행
    private static int dx[] = {0, 0, -1, 1}; //열
    private static int graph[][];
    private static int totalSnakeCnt;

    public static void main(String[] args) {
        //각 테스트케이스에 대해 필요한 최소 배추흰지렁이를 출력해야 한다.
        FastScan scanner = new FastScan();

        int T = Integer.parseInt(scanner.next());

        //테스트 케이스 만큼 반복
        for (int i = 0; i < T; i++) {
            //가로 M, 세로 N, 배추 심어져 있는 위치 k 를 입력받는다.
            int M = Integer.parseInt(scanner.next());
            int N = Integer.parseInt(scanner.next());
            int k = Integer.parseInt(scanner.next());

            totalSnakeCnt = 0;
            graph = new int[M][N];

            // 배추가 심어져 있는 갯수만큼 좌표 x(열), y(행)를 입력 받으며 해당 좌표의 
            // 2차원 배열 값을 1로 초기화 한다.
            for (int j = 0; j < k; j++) {
                int y = Integer.parseInt(scanner.next());
                int x = Integer.parseInt(scanner.next());
                graph[y][x] = 1;
            }

            // 초기화 한 그래프를 돈다.
            for (int y = 0; y < graph.length; y++) {
                for (int x = 0; x < graph[0].length; x++) {
                    if (graph[y][x] == 1) {
                        graph[y][x] = 2;
                        bfs(new Point(y, x));
                    }
                }
            }

            System.out.println(totalSnakeCnt);
        }
    }

    public static void bfs(Point point) {
        // 만약 그래프 값이 2(기방문) 혹은 0 (벽)가 아니면. (방문하면서 미리 값을 바꿀것임 방문 체크를 할 것임.)
        Queue<Point> queue = new LinkedList<>();

        //시작할 위치를 큐에 넣어준다.
        queue.add(point);

        while (!queue.isEmpty()) {
            Point currentPoint = queue.poll();

            int curY = currentPoint.y;
            int curX = currentPoint.x;

            //상,하,좌,우를 탐색 한다.
            for (int i = 0; i < 4; i++) {
                int ny = curY + dy[i];
                int nx = curX + dx[i];

                if (ny < 0 || ny >= graph.length || nx < 0 || nx >= graph[0].length) {
                    continue;
                }

                if (graph[ny][nx] == 0 || graph[ny][nx] == 2) {
                    continue;
                }

                //방문 처리
                //큐에 해당 위치 삽입
                if (graph[ny][nx] == 1) {
                    graph[ny][nx] = 2;
                    queue.add(new Point(ny, nx));
                }
            }
        }
        totalSnakeCnt++;
    }


    public static class Point {
        int y;
        int x;

        public Point(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }


    public static class FastScan {
        BufferedReader br;
        StringTokenizer st;

        public FastScan() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            try {
                while (st == null || !st.hasMoreElements()) {
                    st = new StringTokenizer(br.readLine());
                }
            } catch (Exception e) {
                e.printStackTrace();
            }
            return st.nextToken();
        }
    }
}
