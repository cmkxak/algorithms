import math
def solution(n):
    arr = [True for i in range(n+1)]

    #에라토스테네스의 체 알고리즘 수행
    for i in range(2,int(math.sqrt(n) +1)):
        if arr[i] == True: #남은 수가 소수라면
            j = 2
            while i*j <= n:
                arr[i * j] = False
                j=j+1
    count = 0
    for i in range(2, n+1):
        if arr[i]:
            count+=1
    return count