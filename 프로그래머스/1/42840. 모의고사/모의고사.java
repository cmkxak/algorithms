import java.util.*;

class Solution {
    private static int MAX = 0;
    private static int[] studentScores = new int[3];
    
    public int[] solution(int[] answers) {
        int[] stu1 = {1,2,3,4,5};
        int[] stu2 = {2,1,2,3,2,4,2,5};
        int[] stu3 = {3,3,1,1,2,2,4,4,5,5};
                    
        int stu1Score = getStuScore(answers, stu1, 0);
        int stu2Score = getStuScore(answers, stu2, 1);
        int stu3Score = getStuScore(answers, stu3, 2);
        
        updateMaxScore(studentScores);
        
        int maxScoreStudentCnt = getMaxScoreStudentCnt(studentScores);

        return getMaxScoreStudentList(studentScores, maxScoreStudentCnt);
    }
    
    private void updateMaxScore(int[] studentScores){
        for (int i = 0; i < studentScores.length; i++){
            MAX = Math.max(MAX, studentScores[i]);
        }
    }
    
    private int getStuScore(int[] answers, int[] studentAnswers, int studentIdx){
        int score = 0;
        int n = studentAnswers.length;
        for (int i = 0; i < answers.length; i++){
            if (answers[i] == studentAnswers[i % n]) {
                score++;
            }
        }
        studentScores[studentIdx] = score;
        return score;
    }
    
    private int getMaxScoreStudentCnt(int[] studentScores){
        int size = 0;
        for (int i = 0; i < studentScores.length; i++){
            if (studentScores[i] == MAX) size++;
        }
        return size;
    }
    
     private int[] getMaxScoreStudentList(int[] studentScores, int size){
        int[] answer = new int[size];
        int idx = 0;
        for (int i = 0; i < studentScores.length; i++){
            if (studentScores[i] == MAX){
                answer[idx++] = i + 1;
            }
        }
        return answer;
    }
}