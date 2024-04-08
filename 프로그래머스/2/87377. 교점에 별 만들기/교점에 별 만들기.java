import java.util.*; 

class Solution {
    public String[] solution(int[][] line) {
        //1. 직선의 교점들을 구하고, 그 중 정수 교점만 리스트에 넣어준다.
        List<Point> points = new ArrayList<>();
        
        for (int i = 0; i < line.length; i++){
            for (int j = i + 1; j < line.length; j++){
                Point p = interSection(line[i][0], line[i][1], line[i][2], line[j][0], line[j][1], line[j][2]);
                if (p != null) points.add(p);
            }
        }
        
        //최대,최소 길이를 구해주어 최소 직사각형의 크기를 구해준다.
        Point max = getMaximumPoint(points);
        Point min = getMinimumPoint(points);
        System.out.println(max.x);
        System.out.println(max.y);
        System.out.println(min.x);
        System.out.println(min.y);
        
        //격자판은 무한히 넓으니 모든 별을 포함하는 최소한의 크기만 나타내면 된다.
        int width = (int) (max.x - min.x + 1); 
        int height = (int) (max.y - min.y + 1);
        
        char[][] c = new char[height][width];
        
        System.out.println(width);
        System.out.println(height);
        
        for (char[] arr : c){
            Arrays.fill(arr, '.');
        }
        
        for (Point p : points){
            int x = (int) (p.x - min.x);
            int y = (int) (max.y - p.y);
            
            c[y][x] = '*';
        }
        
        String result[] = new String[c.length];
        for (int i = 0; i< result.length; i++){
            result[i] = new String(c[i]);
        }
        
        
        return result;
    }
    
    private Point getMaximumPoint(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point p : points){
            if (p.x > x) x = p.x;
            if (p.y > y) y = p.y;
        }
        return new Point(x, y);
    }
    
    private Point getMinimumPoint(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point p : points){
            if (p.x < x) x = p.x;
            if (p.y < y) y = p.y;
        }
        return new Point(x, y);
    }
        
        
    //주어진 직선 정보들을 통해 두 직선의 교점을 구해준다.
    private Point interSection(long a, long b, long e, long c, long d, long f){
        double x = (double) (b * f - e * d) / (a * d - b * c);
        double y = (double) (e * c - a * f) / (a * d - b * c);
        if (x % 1 != 0 || y % 1 != 0){
            return null;
        }   
        return new Point((long) x, (long)y);
    } 
    
    
    //교점을 구하기 위한 클래스 생성
    static class Point{
        long x;
        long y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
}