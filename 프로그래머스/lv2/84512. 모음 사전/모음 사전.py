from itertools import product
def solution(word):
    answer = 0
    alphabet = ['A', 'E', 'I', 'O', 'U']
    
    candidates = []
    for i in range(1,6):
        for j in product(alphabet, repeat = i):
            candidates.append(list(j))
    
    candidates.sort()
    
    return candidates.index(list(word)) + 1
