import java.util.*;

class Solution {
    
    private static int dy[] = {-1,0,0,1};
    private static int dx[] = {0,-1,1,0};
    
    public int[] solution(String[][] places) {
        int[] answer = new int[places.length];
        
        for (int i = 0; i < answer.length; i++){
            String[] place = places[i];
            
            char[][] graph = new char[places.length][]; 
            for (int j = 0 ; j < graph.length; j++){
                graph[j] = place[j].toCharArray();
            }
            
            if (isDistanced(graph)){
                answer[i] = 1;
            } else {
                answer[i] = 0;
            }
        }
        return answer;
    }
    
    public boolean isDistanced(char[][] graph){
        for (int y = 0; y < graph.length; y++){
            for (int x = 0; x < graph[y].length; x++){
                if (graph[y][x] != 'P') continue;
                
                if (!isDistancedEachOther(y, x, graph)) 
                    return false;
            }
        }
        return true;
    }

    public boolean isExistParticipantNearBy(int y, int x, char[][] places, int start){
        for (int i = 0; i < 4; i++){
            if (i == start) 
                continue;
            
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            //행과 열 순서대로 조건을 나열해야 한다.
            if (ny < 0 || ny >= places.length || nx < 0 || nx >= places[ny].length) 
                continue; 
            
            if (places[ny][nx] == 'P') {
                return true;
            }
        }
        
        return false;
    }
    
    public boolean isDistancedEachOther(int y, int x, char[][]places){
        for (int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            
            if (ny < 0 || ny >= places.length || nx < 0 || nx >= places[ny].length) 
                continue; 
            
            if (places[ny][nx] == 'O') {
                if (isExistParticipantNearBy(ny, nx, places, 3-i)) 
                    return false;
            }
            
            if (places[ny][nx] == 'P') {
                return false;
            }
        }
        
        return true;
    }
}