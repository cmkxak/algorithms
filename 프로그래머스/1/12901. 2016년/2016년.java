import java.time.*;
import java.time.format.TextStyle;
import java.util.Locale;

class Solution {
    public String solution(int a, int b) {
        LocalDate date = LocalDate.of(2016, a, b);
        DayOfWeek week = date.getDayOfWeek();
        return week.getDisplayName(TextStyle.SHORT, Locale.US).toUpperCase();
    }
}