import java.io.*;
import java.util.*;

public class Main {

    private static boolean isDfsVisited[];
    private static boolean isBfsVisited[];
    private static List<Integer>[] graph;

    public static void main(String[] args) {
        FastScan fastScan = new FastScan();

        int N = fastScan.nextInt(); //노드의 수
        int M = fastScan.nextInt(); //간선의 수
        int V = fastScan.nextInt(); // 탐색을 시작할 정점 번호

        graph = new ArrayList[N + 1];
        isDfsVisited = new boolean[N + 1];
        isBfsVisited = new boolean[N + 1];

        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        //정점간의 연결된 간선들을 입력받는다.
        //인접 정점을 초기화한다.
        for (int i = 0; i < M; i++) {
            int fromNode = fastScan.nextInt();
            int toNode = fastScan.nextInt();
            graph[fromNode].add(toNode);
            graph[toNode].add(fromNode);
        }
        
        //숫자가 작은 인접 정점부터 방문해야 하므로 각 정점의 인접 정점 리스트를 오름차순 정렬한다.
        for (int i = 1; i < graph.length; i++) {
            Collections.sort(graph[i]);
        }

        dfs(V, 0, N);
        System.out.println();
        bfs(V);
    }


    public static void dfs(int startNode, int depth, int N) {
        isDfsVisited[startNode] = true;
        System.out.printf(startNode + " ");

        for (int i = 0; i < graph[startNode].size(); i++) {
            int adjacentNode = graph[startNode].get(i);
            if (!isDfsVisited[adjacentNode]) {
                if (depth == N - 1) {
                    return;
                }
                dfs(adjacentNode, depth + 1, N);
            }
        }
    }

    public static void bfs(int start) {
        StringBuilder sb = new StringBuilder();
        Queue<List<Integer>> queue = new LinkedList<>();

        sb.append(start).append(" ");
        isBfsVisited[start] = true;

        queue.add(graph[start]);

        while (!queue.isEmpty()) {
            List<Integer> adjecentNodes = queue.poll();

            for (int i = 1; i <= adjecentNodes.size(); i++) {
                if (isBfsVisited[adjecentNodes.get(i - 1)]) {
                    continue;
                } else {
                    sb.append(adjecentNodes.get(i - 1)).append(" ");
                    isBfsVisited[adjecentNodes.get(i - 1)] = true;
                    queue.add(graph[adjecentNodes.get(i - 1)]);
                }
            }
        }
        System.out.println(sb.toString());
    }

    public static class FastScan {
        BufferedReader br;
        StringTokenizer st;

        public FastScan() {
            this.br = new BufferedReader(new InputStreamReader(System.in));
        }

        public String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        public int nextInt() {
            return Integer.parseInt(next());
        }
    }


}
