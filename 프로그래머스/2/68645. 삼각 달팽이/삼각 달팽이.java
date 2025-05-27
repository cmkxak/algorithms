import java.util.*;

class Solution {
    
    //방향 정의
    private static final int dy[] = {1, 0, -1};
    private static final int dx[] = {0, 1, -1};
    
    public int[] solution(int n) {
        //1. 2차원 그래프 생성
        int graph[][] = new int[n][n];
        
        //2. 시작 좌표, 방향 인덱스 좌표, 초기값 생성
        int y = 0;
        int x = 0;
        int dir = 0;
        int v = 1;
            
        //3. 달팽이 이동
        while (true) {
            //4. 이동 처리 및 다음 방향 선정
            graph[y][x] = v++;
            int ny = y + dy[dir];
            int nx = x + dx[dir];
        
            //4.1 새로 이동한 방향이 범위가 벗어나거나 이미 방문한 경우
            if (nx == n || ny == n || nx == -1 || ny == -1 || graph[ny][nx] != 0) {
                //4.1.1 방향 전환
                dir = (dir + 1) % 3;
                ny = y + dy[dir];
                nx = x + dx[dir];
                
                //4.1.2 전환된 방향이 이동할 수 있는지 검증
                if (nx == n || ny == n || nx == -1 || ny == -1 || graph[ny][nx] != 0) break;
            }
            
            //5. 이동된 좌표로 초기화
            y = ny;
            x = nx;
        }
        
        //6. 1차원 결과 배열 생성
        int answer[] = new int[v-1];
        
        int idx = 0;
        for (int i = 0; i < n; i++){
            for (int j = 0; j <=i; j++){
                //7. 달팽이 이동을 통해 채워진 값 -> 정답 배열에 할당
                answer[idx++] = graph[i][j];
            }
        }
        
        //8. 정답 리턴
        return answer;
    }
}