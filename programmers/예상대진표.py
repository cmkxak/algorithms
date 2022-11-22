import math

def solution(n,a,b):
    answer = 0

    while a!=b: # 제약 조건 -> a와 b가 같지 않을 동안
        a = math.ceil(a/2) # 참가자 수 감소
        b = math.ceil(b/2) # 경쟁자 수 감소
        answer+=1 # 라운드 수 + 1

    return answer # 증가된 총 라운드 수 반환