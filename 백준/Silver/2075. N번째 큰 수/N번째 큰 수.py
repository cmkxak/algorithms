import heapq
n = int(input())
graph = []
for i in range(n):
    numbers = map(int, input().split())
    for num in numbers:
        if len(graph) < n:
            heapq.heappush(graph, num)
        else:
            if graph[0] < num:
                heapq.heappop(graph)
                heapq.heappush(graph, num)
print(graph[0])