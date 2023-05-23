def solution(n):
    answer = 0
    MAX_RANGE = 1_000_001
    oneCnt = bin(n)[2:].count('1')
    for i in range(n+1, MAX_RANGE):
        if oneCnt == bin(i)[2:].count('1'):
            answer=i
            break
    return answer