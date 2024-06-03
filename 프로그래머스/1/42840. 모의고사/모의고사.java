import java.util.*;

class Solution {
    private static int MAX_SCORE = 0;
    private static final int[] scoreBoard = new int[3];
    private ArrayList<Integer> answer = new ArrayList<>();
    private int idx = 0;
    
    public int[] solution(int[] answers) {
        
        int[] stu1 = new int[]{1,2,3,4,5};
        int[] stu2 = new int[]{2,1,2,3,2,4,2,5};
        int[] stu3 = new int[]{3,3,1,1,2,2,4,4,5,5};
      
        getEachStuScore(stu1, answers, scoreBoard);
        getEachStuScore(stu2, answers, scoreBoard);
        getEachStuScore(stu3, answers, scoreBoard);
        setMaxScore(scoreBoard);
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    public void getEachStuScore(int[] stuScore, int[] answers, int[] board){
        int score = 0;
        
        for (int i = 0; i < answers.length; i++){
            if (stuScore[i % stuScore.length] == answers[i])
                score++;
        }
        board[idx++] = score;
        MAX_SCORE = Math.max(MAX_SCORE, score);
    }
    
    public void setMaxScore(int[] board){
        for (int i = 0; i< board.length; i++){
            if (board[i] == MAX_SCORE) 
                answer.add(i+1);
        }
    }
     
}