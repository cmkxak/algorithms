import java.util.*;

class Solution {
    private static final int dx[] = {0,1,-1};
    private static final int dy[] = {1,0,-1};
    
    public int[] solution(int n) {
        
        int[][] answer = new int[n][n];
        
        int x =0;
        int y =0;
        int i = 1;
        int d = 0;
        
        while(true){
            
            answer[y][x] = i++;
            int nx = x + dx[d];
            int ny = y + dy[d];
            
            if (ny == n || nx == n || answer[ny][nx] !=0 ){
                //방향 전환
                d = (d+1) % 3;
                nx = x + dx[d];
                ny = y + dy[d];
                
                //전환된 방향으로도 진행을 하지 못하는 경우 : 마지막 숫자의 경우
                if(ny == n || nx == n || answer[ny][nx] !=0 ) break;  
            }
            x = nx;
            y = ny;
        }
        
        
        int result[] = new int[i-1];
        int idx = 0;
        for (int k =0; k< n; k++){
            for (int j = 0; j <= k; j++){
                result[idx++] = answer[k][j];
            }
        }
        
        return result;
    }
}