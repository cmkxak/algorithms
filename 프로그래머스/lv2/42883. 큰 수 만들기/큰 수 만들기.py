def solution(number, k):
    answer = ''
    number=list(number)
    print(number)
    
    min=int(1e9)
    for i in range(len(number)):
        if min > int(number[i]):
            min=int(number[i])
            number.remove(number[i])
    print(number)
    
    
    
    return answer