def solution(food):
    answer = ''
    repeat = 0
    food_dict = {str(i):food[i] for i in range(1,len(food))}
    
    for key,val in food_dict.items():
        answer += key * (val // 2)
        
    answer += '0' + answer[::-1]
    return answer