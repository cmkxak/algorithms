def solution(strings, n):
    answer = sorted(strings, key=lambda x:(x[n], str(x)))
    return answer