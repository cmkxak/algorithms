import java.util.*;

class Solution {
    public String[] solution(int[][] line) {
        List<Point> intersactions = new ArrayList<>();
        
        for (int i =0; i < line.length;i++) {
            for (int j = i + 1; j < line.length; j++){
                int lines[] = line[i];
                int lines2[] = line[j];
                
                Point point = interSection(lines[0], lines[1], lines[2], lines2[0], lines2[1], lines2[2]);
                
                //교점이 정수라면
                if (point != null) {
                    intersactions.add(point);
                }
            }
        }
        
        //2. 좌표의 최대 / 최소값 구하기
        Point minPoint = getMinPoint(intersactions);
        Point maxPoint = getMaxPoint(intersactions);
        
        
        //3. 구한 최대/최솟값으로 2차원 배열 생성
        int width = (int) (maxPoint.x - minPoint.x + 1);
        int height = (int) (maxPoint.y - minPoint.y + 1);
        
        char[][] arr = new char[height][width];
        
        //4. 2차원 배열의 크기만큼 순회하며 '.'으로 초기화
        for (char[] row : arr){
            Arrays.fill(row, '.');
        }    
            
        //5. 2차원 배열에 별찍기
        //2차원 배열에서 0,0은 실제 교점이 아님, 
        //교점을 표현할 수 있는 가장 작은 크기로 2차원 배열 선언, 별을 제대로 표시하려면 좌표를 변환시켜야 한다
        for (Point p : intersactions) {
            int y = (int) (maxPoint.y - p.y);
            int x = (int) (p.x - minPoint.x);
            arr[y][x] = '*';
        }
        
        //6. 2차원 배열 내 있는 문자들을 문자열 배열로 변환후 반환
        String[] answer = new String[arr.length];
        
        for (int i = 0; i < answer.length; i++){
            answer[i] = new String(arr[i]);
        }
        
        return answer;
    }
    
    private Point getMinPoint(List<Point> points){
        long x = Long.MAX_VALUE;
        long y = Long.MAX_VALUE;
        
        for (Point p : points) {
            if (p.x < x) x = p.x;
            if (p.y < y) y = p.y;
        }
        
        return new Point(x,y);
    }
    
    private Point getMaxPoint(List<Point> points){
        long x = Long.MIN_VALUE;
        long y = Long.MIN_VALUE;
        
        for (Point p : points) {
            if (p.x > x) x = p.x;
            if (p.y > y) y = p.y;
        }
        
        return new Point(x,y);
    }
    
    private Point interSection(long a, long b, long e, long c, long d, long f) {
        double x = (double) (b*f - e*d) / (a*d - b*c);
        double y = (double) (e*c - a*f) / (a*d - b*c);
        
        //정수가 아니면 null
        if (x % 1 != 0 || y % 1 != 0) 
            return null;
        
        return new Point((long) x, (long) y);
    }
    
    
    class Point {
        long x;
        long y;
        
        public Point(long x, long y){
            this.x = x;
            this.y = y;
        }
    }
}