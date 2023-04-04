#피보나치 함수
zero = [1,0,1] #0 호출횟수, 각 인덱스 숫자일 때 0이 호출되는 횟수가 저장됨
one = [0,1,1] #1 호출횟수, 각 인덱스 숫자일 때 1이 호출되는 횟수가 저장됨

def fibo(n):
    length = len(zero)

    if n >= length:
        for i in range(length, n+1):
            zero.append(zero[i-1] + zero[i-2]) # 2 1 3일떄는 fibo(2)의 0호출 횟수, fibo(1)의 0호출 횟수를 더해준 것과 같다
            one.append(one[i-1] + one[i-2])
    print(f'{zero[n]} {one[n]}')

t=int(input())
for _ in range(t):
    n = int(input())
    fibo(n)