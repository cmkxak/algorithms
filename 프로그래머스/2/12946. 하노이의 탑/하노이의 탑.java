import java.util.*;

class Solution {
    private static ArrayList<int[]> moveInfo = new ArrayList<>();
    
    public int[][] solution(int n) {
        hanoi(1, 2, 3, n);
        
        return moveInfo.toArray(new int[moveInfo.size()][]);
    }
    
    public void hanoi(int start, int m, int to, int n){
        if (n == 0) return;
        
        hanoi(start, to, m, n-1);
        moveInfo.add(new int[]{start, to});
        hanoi(m, start, to, n-1);
    }
}