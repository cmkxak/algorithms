from collections import deque
def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    while queue:
        m = max(queue)
        l = queue.popleft()
        #변수 l에 저장하면서 popleft()했으므로 타겟 프로세스의 위치가 1 줄어들었다. 고로, location--
        location-=1
        
        if l!=m:
            queue.append(l)
            if location < 0:
                location = len(queue)-1
        else:
            answer+=1
            print("현재 값:", l, answer, location)
            if location<0:
                break
        print(queue)
    return answer