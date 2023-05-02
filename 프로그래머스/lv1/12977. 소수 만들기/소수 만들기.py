from itertools import combinations
def is_prime(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
    if is_prime:
        return True
    else:
        return False
    
def solution(nums):
    answer = 0
    candidates = list(combinations(nums, 3))
    for i in candidates:
        if is_prime(sum(i)):
            answer+=1
    return answer