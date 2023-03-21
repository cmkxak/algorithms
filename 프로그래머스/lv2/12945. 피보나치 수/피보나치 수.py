def fibo(n):
    fibo_lst=[0] * (n+1)
    fibo_lst[1]=1
    fibo_lst[2]=1
    for i in range(3,n+1):
        fibo_lst[i] = fibo_lst[i-2] + fibo_lst[i-1]
    return fibo_lst[n]%1234567

def solution(n):
    answer = fibo(n)
    return answer