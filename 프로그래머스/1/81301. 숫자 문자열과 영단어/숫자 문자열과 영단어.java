import java.util.*;

class Solution {
    public int solution(String s) {
        ArrayList<String> info = new ArrayList<>();
        info.add("zero");
        info.add("one");
        info.add("two");
        info.add("three");
        info.add("four");
        info.add("five");
        info.add("six");
        info.add("seven");
        info.add("eight");
        info.add("nine");
        
        for (int i = 0; i< info.size(); i++){
            if (s.contains(info.get(i))){
                System.out.println(info.get(i));
                s = s.replaceAll(info.get(i), Integer.toString(i));
            }
        }
        return Integer.parseInt(s);
    }
}