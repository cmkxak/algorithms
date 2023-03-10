dp=[0] * 100

#재귀함수 종료조건 무조건 중요
def fibo(x):

    print("f(" + str(x) + ")")
    if x == 1 or x == 2:
        return 1

    #한번 계산된 결과는 저장된 값을 바로 반환
    if dp[x] != 0:
        return dp[x]
    # 아직 계산되지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    return fibo(x-2) + fibo(x-1)
    return dp[x]
print(fibo(99))
