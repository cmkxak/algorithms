def convert(n, base):
    T = '0123456789ABCDEF'
    q,r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q,base) + T[r]

def solution(n, t, m, p):
    answer = ''
    candidates = []
    
    #전체 n진수 갯수
    for i in range(t * m):
        res = convert(i, n)
        for r in res:
            candidates.append(r)
    
    #튜브가 미리 구할 숫자의 갯수
    for i in range(p-1, len(candidates), m):
        answer+= candidates[i]
        if len(answer) >= t:
            break
    return answer
        
        
    
