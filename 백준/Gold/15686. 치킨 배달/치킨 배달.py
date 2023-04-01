from itertools import combinations

n,m=map(int, input().split())
chicken, house= [],[]

for r in range(n):
    data=list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c)) #일반 집
        elif data[c] == 2:
            chicken.append((r,c)) #치킨 집

candidates = list(combinations(chicken, m)) #치킨집이 m개만 남는 경우의 수

result = 1e9
for c in candidates:
    dist = 0
    tmp = 0
    for hx, hy in house:
        res= 1e9
        for j in range(m):
            #남는 치킨집의 조합에서 모든 집과 치킨집간의 치킨 거리를 구하여 최솟값을 구한다.
            res = min(res, abs(c[j][0]-hx) + abs(c[j][1] - hy)) #치킨 거리 계산
        dist+=res #모든 집의 치킨 거리 
    result = min(result, dist)
print(result)