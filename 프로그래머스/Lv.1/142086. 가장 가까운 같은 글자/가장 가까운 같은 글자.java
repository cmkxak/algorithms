import java.util.*;

class Solution {
    public int[] solution(String s) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(-1);

        for (int i = 1; i < s.length(); i++) {
            String frontStr = s.substring(0, i);
            String now = String.valueOf(s.charAt(i));
            if (frontStr.contains(now)) {
                answer.add(i - s.lastIndexOf(now, i-1));
            } else {
                answer.add(-1);
            }
        }

        return answer.stream().mapToInt(Integer::intValue)
                .toArray();
    }
}