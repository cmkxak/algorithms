class Solution {
    public String solution(String X, String Y) {
        StringBuilder answer = new StringBuilder();
        
        int xNums[] = new int[10];
        int yNums[] = new int[10];
        
        //X,Y에 등장하는 숫자의 개수를 xNums, yNums에 체크
        checkNum(X,xNums);
        checkNum(Y, yNums);
        
        for(int i = xNums.length-1; i>=0; i--){
            while(xNums[i] >= 1 && yNums[i] >= 1){
                answer.append(i);
                xNums[i]--;
                yNums[i]--;
            }
        }
        
        if (answer.toString().equals("")){
            return "-1";
        } else if (answer.toString().startsWith("0")){ //0만 여러개 존재하는 경우를 방지하기 위해.
            return "0";
        } else {
            return answer.toString();
        }
    }
    
    public void checkNum(String x, int[] args){
        for(int i=0; i<x.length(); i++){
            int idx = x.charAt(i) - '0'; //이 위치에 수가 있다고 체크
            args[idx]++;
        }
    }
}