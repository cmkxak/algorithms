import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length - 5];
        
        //1. 배열 정렬 [선택 정렬]
        int idx = 0;
        
        for(int i =0; i< num_list.length - 1; i ++){
            int minIdx = i;
            
            //최솟값의 인덱스 찾기
            for (int j = i+1; j< num_list.length; j++){
                if (num_list[minIdx] > num_list[j]){
                    minIdx = j;
                }
            }
            
            // i번째 값 <-> 찾은 최솟값을 교환
            swap(num_list, minIdx, i);
        }
        
        for (int k = 5 ; k<num_list.length; k++){
            answer[idx++] = num_list[k];
        }
        
        
        return answer;
    }
    
    private static void swap(int[] list, int minIdx, int origin){
        int tmp = list[minIdx];
        list[minIdx] = list[origin];
        list[origin] = tmp;
    }
    
}