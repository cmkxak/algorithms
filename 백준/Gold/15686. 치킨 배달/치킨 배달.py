from itertools import combinations

def check():
    result = 1e9
    for c in chicken_house:
        total_chicken_dist = 0
        for x,y in homes:
            each_dist= 1e9
            for j in range(m):
                #각 집의 치킨 거리
                each_dist = min(each_dist, abs(c[j][0] - x) + abs(c[j][1] - y))
            #도시의 치킨 거리
            total_chicken_dist += each_dist
        result = min(result, total_chicken_dist)
    return result

n,m =map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

#치킨집
chickens = []
homes = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickens.append((i,j))
        #집인 경우
        if graph[i][j] == 1:
            homes.append((i,j))
chicken_house = list(combinations(chickens, m))
print(check())