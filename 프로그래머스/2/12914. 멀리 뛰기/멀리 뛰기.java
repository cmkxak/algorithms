class Solution {
    public long solution(int n) {
        long board[] = new long[n];
    
        if (n == 1)
            return 1;
        board[0] = 1;
        board[1] = 2; 
        for(int i =2; i < n; i++){
            board[i] = (board[i-1] + board[i-2]) % 1234567;
        }
        return board[n-1];
    }
}