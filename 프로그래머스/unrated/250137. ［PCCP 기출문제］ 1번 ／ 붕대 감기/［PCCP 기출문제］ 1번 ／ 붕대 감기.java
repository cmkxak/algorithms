class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        
        int maxHealth = health;
        int success = 0;
        int attackTimeIdx = 0;
        int lastAttackT = attacks[attacks.length-1][0];
        
        for (int i = 1; i<= lastAttackT; i++){
            
            if (i == attacks[attackTimeIdx][0]){
                health -= attacks[attackTimeIdx][1];
                success = 0;
                attackTimeIdx++;
                if (health <= 0) return -1; 
            } else {
                success++;
                health += bandage[1];
                
                if (success == bandage[0]){
                    health += bandage[2];
                    success = 0;
                }
                
                if (health > maxHealth) health = maxHealth;   
            }
        }
        return health;
    }
}