def solution(a, b, n):
    answer = 0
    
    while n > 0:
        returnedCoke = (n//a * b)
        n = n - (a * (n//a)) + ((n//a) * b)
        answer += returnedCoke
        if n < a:
            break
    return answer