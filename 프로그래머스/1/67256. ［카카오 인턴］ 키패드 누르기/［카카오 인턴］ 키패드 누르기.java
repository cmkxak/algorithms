import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    private static class Hand {
        private int x; //열
        private int y;  //행
        private int baseX; //초기 좌표
        public String hand; //각 손의 피아식별
        
        public Hand(int x, String hand){
            this.x = x;
            this.y = 3;
            this.baseX = x;
            this.hand = hand; 
        }
        
        public void move(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
    
    public int calculateDistance(int x, int y, Hand hand){
            if (x == hand.baseX) return 0; 
            return Math.abs(y - hand.y) + Math.abs(x - hand.x);
    }
    
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        Hand left = new Hand(0, "L");
        Hand right = new Hand(2, "R");
        
        return Arrays.stream(numbers)
            .mapToObj(n -> moveHand(n, left, right, hand).hand)
            .collect(Collectors.joining());
    }
    
    public int getX(int num){
        if (num == 0) return 1;
        return (num -1) % 3;
    }
        
    public int getY(int num){
        if (num == 0) return 3;
        return (num-1) / 3;
    }
    
    private Hand moveHand(int n, Hand leftHand, Hand rightHand, String prefer){
            //현재 숫자의 위치 가져오기
            int x = getX(n);
            int y = getY(n);
            
            //거리 계산
            int distanceLeft = calculateDistance(x, y, leftHand);
            int distanceRight = calculateDistance(x, y, rightHand);
            
            Hand hand = null;
            if (distanceLeft == distanceRight){
                if (prefer.equals("right")) hand = rightHand;
                else hand = leftHand;
            } else if (distanceLeft < distanceRight) {
                hand = leftHand;
            } else {
                hand = rightHand;
            }
            
            hand.move(x,y);
            //최종 현재 위치에서 누른 손 반환
            return hand;            
        }
}