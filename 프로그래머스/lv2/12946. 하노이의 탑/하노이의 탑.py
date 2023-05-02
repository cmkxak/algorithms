result = []
def hanoi(n, from_idx, to, aux):
    global result
    if n == 1:
        result.append([from_idx, to]) # 1 3
        return
    hanoi(n-1, from_idx, aux, to) # 2 1 2 3 -> 1 1 3 2 
    result.append([from_idx, to])
    hanoi(n-1, aux, to, from_idx)
    return result

def solution(n):
    return hanoi(n,1,3,2)