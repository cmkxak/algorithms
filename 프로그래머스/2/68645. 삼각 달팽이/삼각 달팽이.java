import java.util.*;

class Solution {
    
    private static final int[]dx = {0,1,-1};
    private static final int[]dy = {1,0,-1};
    public int[] solution(int n) {
        
        int[][] graph = new int[n][n];
        
        int x =0, y = 0;
        int v = 1;
        int i = 0;

        while (true) {
            
            graph[y][x] = v++;
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (nx == n || ny == n ||  nx == -1 || ny == -1 || graph[ny][nx] != 0) {
                i = (i + 1) % 3;
                nx = x + dx[i];
                ny = y + dy[i];
                
                if (nx == n || ny == n || nx == -1 || ny == -1 || graph[ny][nx] != 0) {
                    break;
                }
            }
            y = ny;
            x = nx;
        }
        
        int[] answer = new int[v - 1];
        
        int idx = 0;
        for (int k =0; k<n; k++){
            for (int j = 0; j <= k; j++){
                answer[idx++] = graph[k][j]; 
            }
        }
        
        
        return answer;
    }
}