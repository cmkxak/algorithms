class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int answer1 = 1;
        
        int size = num_list.length;
        
        if (size >= 11){
            for(int num : num_list){
                answer += num;
            }
            return answer;
        } else {
            for(int num : num_list){
                answer1 *= num;
            }
            return answer1;
        }
    }
}