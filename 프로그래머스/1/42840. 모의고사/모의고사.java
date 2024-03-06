import java.util.*;

class Solution {
    private int getMaxScore(int[] stuScore){
        int maxScore = 0;
        for (int i =0; i<stuScore.length; i++){
            maxScore = Math.max(maxScore, stuScore[i]); 
        }
        return maxScore;
    }
    
    public int[] solution(int[] answers) {
        int stuScore[] = {0,0,0};
        
        int stu1[] = {1,2,3,4,5};
        int stu2[] = {2,1,2,3,2,4,2,5};
        int stu3[] = {3,3,1,1,2,2,4,4,5,5};
        
        int stu1Idx = 0;
        int stu2Idx = 0;
        int stu3Idx = 0;
        
        for (int i = 0; i < answers.length; i++){ 
            if (answers[i] == stu1[i%5]){
                stuScore[0]++;
            } 
            
            if (answers[i] == stu2[i%8]){
                stuScore[1]++;
            }
            
            if (answers[i] == stu3[i%10]){
                stuScore[2]++;
            }
        }
        
        int maxScore = getMaxScore(stuScore);
        
        ArrayList<Integer> resultList = new ArrayList<>();
        for(int i = 0; i<stuScore.length; i++){
            if (maxScore == stuScore[i])
                resultList.add(i+1);
        }
        
        return resultList.stream().mapToInt(Integer::intValue).toArray();
    }
}