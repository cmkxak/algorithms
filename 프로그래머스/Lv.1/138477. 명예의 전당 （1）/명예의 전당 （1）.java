import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        ArrayList<Integer> answer = new ArrayList<>();
        int[] result = new int[score.length];

        result[0] = score[0];
        answer.add(score[0]);

        for (int i =1; i<score.length;i++){

            if (i > k-1){
                answer.add(score[i]);
                Collections.sort(answer);
                result[i] = answer.get(i-k+1);
            } else {
                answer.add(score[i]);
                Collections.sort(answer);
                result[i] = answer.get(0);
            }
        }

        return result;
    }
}