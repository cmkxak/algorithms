class Solution {
    public int[] solution(int[][] arr) {
        QuadAppchuck answer = recursive(0, 0, arr.length, arr);
        return new int[]{answer.zero, answer.one};
    }
    
    public QuadAppchuck recursive(int x, int y, int size, int arr[][]) {
        //종료조건
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                //조건이 같지 않은 경우
                if (arr[i][j] != arr[x][y]) {
                    return recursive(x, y, size / 2, arr) //위 왼쪽
                            .add(recursive(x + size / 2, y, size / 2, arr)) //위 오른쪽
                            .add(recursive(x, y + size / 2, size / 2, arr)) //아래 왼쪽
                            .add(recursive(x + size / 2, y + size / 2, size / 2, arr)); //아래 오른쪽

                }
            }
        }

        if (arr[x][y] == 1) {
            return new QuadAppchuck(0, 1);
        } else {
            return new QuadAppchuck(1, 0);
        }
    }
    
    static class QuadAppchuck {

        private int zero;
        private int one;

        public QuadAppchuck(int zero, int one) {
            this.zero = zero;
            this.one = one;
        }

        public QuadAppchuck add(QuadAppchuck other) {        
            return new QuadAppchuck(this.zero + other.zero, this.one + other.one);
        }
    }
}