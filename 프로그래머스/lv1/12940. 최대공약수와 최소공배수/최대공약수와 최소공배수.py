def gcd(n,m): 
    mod = n % m #2
    while mod > 0:
        n = m 
        m = mod
        mod = n % m
    return m
        
def solution(n, m):
    answer = []
    
    #최대 공약수
    answer.append(gcd(n,m))
    
    #최소 공배수
    answer.append(n*m / gcd(n,m))
    return answer