import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for i in scoville:
        heapq.heappush(q, i)
    
    while q[0] < K:
        heapq.heappush(q, heapq.heappop(q) + (heapq.heappop(q) * 2))
        answer+=1
    	
        if len(q) == 1 and q[0] < K:
            return -1
    return answer