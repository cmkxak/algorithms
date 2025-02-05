import java.util.*;

class Solution {
    
    private static List<Point> points = new ArrayList<>();
    
    public String[] solution(int[][] line) {
        for (int i = 0; i < line.length - 1; i++){
            for (int j = i + 1; j < line.length; j++){
                setInterSection(line[i], line[j]);
            }
        }
        
        Point minimumPoint = getMinimumPoint();
        Point maximumPoint = getMaximumPoint();
        
        int width = (int) (maximumPoint.x - minimumPoint.x + 1);
        int height = (int) (maximumPoint.y - minimumPoint.y + 1);
        
        char[][] arr = new char[height][width];
        
        for (char[] row : arr) {
            Arrays.fill(row, '.');
        }
        
        for (Point p : points){
            int x = (int) (p.x - minimumPoint.x);
            int y = (int) (maximumPoint.y - p.y);
            arr[y][x] = '*';
        }
        
        String answer[] = new String[arr.length];
        
        for (int i =0; i < answer.length; i++){
            answer[i] = new String(arr[i]);
        }
        
        return answer;
    }
    
    private Point getMinimumPoint(){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point point : points) {
            if (x > point.x) x = point.x;
            if (y > point.y) y = point.y;
        }
        
        return new Point(x,y);
    }
    
    private Point getMaximumPoint(){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point point : points) {
            if (x < point.x) x = point.x;
            if (y < point.y) y = point.y;
        }
        
        return new Point(x,y);
    }
    
    public void setInterSection(int[] line1, int[] line2){
        long a = line1[0];
        long b = line1[1];
        long e = line1[2]; 
        
        long c = line2[0];
        long d = line2[1];
        long f = line2[2];        
        
        long x = 1000;
        long y = 1000;
        
        long divideNum = (a * d) - (b * c);
        
        if (divideNum != 0) {
            if (((b * f) - (e * d)) % ((a * d) - (b * c)) == 0)
                x = ((b * f) - (e * d)) / ((a * d) - (b * c));
        
            if (((e * c) - (a * f)) % ((a * d) - (b * c)) == 0)
                y = ((e * c) - (a * f)) / ((a * d) - (b * c));
        }
        
        //x,y가 정수이면 * 표시를 위해 points 리스트에 add.
        if (x != 1000 && y != 1000)
            points.add(Point.createPoint(x,y));
    }
    
    
    
    static class Point {
        long x;
        long y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
        public static Point createPoint(long x, long y){
            return new Point(x, y);
        }
    }
}