def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for name, t in clothes:
        clothes_dict[t] = clothes_dict.get(t, 0) + 1
    
    for value in clothes_dict.values():
        answer *= value + 1
    
    return answer-1