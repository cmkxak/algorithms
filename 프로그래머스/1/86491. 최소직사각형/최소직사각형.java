class Solution {
    public int solution(int[][] sizes) {
        //1. 가로에 큰 길이를 모두 몰아준다.
        for (int i = 0; i < sizes.length; i++){
            int tmp = 0;
            if (sizes[i][0] < sizes[i][1]){
                tmp = sizes[i][0];
                sizes[i][0] = sizes[i][1];
                sizes[i][1] = tmp;
            }
        }
        
        //2. 가로길이 중 가장 큰 길이와 세로 가장 큰 길이의 곱을 리턴.
        int wMax = 0;
        int hMax = 0;
        
        for(int i =0; i< sizes.length; i++){
            if (wMax < sizes[i][0]){
                wMax = sizes[i][0];
            }
            if (hMax < sizes[i][1]){
                hMax = sizes[i][1];
            }
        }

        return wMax * hMax;
    }
}